ip=''
while True:
    try:
        p=raw_input()
    except:
        break
    ip+=p.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    print i +' : '+ str(ip.count(i))