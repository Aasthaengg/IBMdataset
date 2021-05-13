c = 0
hoge = ''
while True:
    sent = input()
    if sent.strip() == 'END_OF_TEXT':
        break
    if hoge:
        for word in sent.split():
            if word.lower() == hoge:
                c += 1
    else:
        hoge = sent.strip()
print (c)
