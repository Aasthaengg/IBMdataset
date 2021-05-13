docs = ''
while True:
    try:
        s = raw_input()
    except:
        break
    docs += s.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    print i +' : '+ str(docs.count(i))