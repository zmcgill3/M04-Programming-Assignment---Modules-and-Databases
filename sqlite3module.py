import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS books
    (title TEXT,
     author TEXT,
     year INT)''')
ins = 'INSERT INTO books (title, author, year) VALUES(?, ?, ?)'
curs.execute(ins, ('The Weirdstone of Brisingamen','Alan Garner',1960))
curs.execute(ins, ('Perdido Street Station','China Miéville',2000))
curs.execute(ins, ('Thud!','Terry Pratchett',2005))
curs.execute(ins, ('The Spellman Files','Lisa Lutz',2007))
curs.execute(ins, ('Small Gods','Terry Pratchett',1992))

curs.execute('SELECT * FROM books ORDER BY title')
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()