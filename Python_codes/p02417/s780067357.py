s = ""
while True:
    try:
        s += input()
    except:
        break
    
l = list(s.lower())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
c = [l.count(alphabet[i]) for i in range(26)]
for i in range(26):
    print("{} : {}".format(alphabet[i],c[i]))