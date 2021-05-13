alphabet = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for ch in alphabet:
    dic[ch] = 0
    
while True:
    try:
        st = raw_input()
    except EOFError:
        break

    for ch in st:
        try:
            dic[ch.lower()] +=1
        except:
            pass
for k in sorted(dic.keys()):
    print k +' : ' + str(dic[k])