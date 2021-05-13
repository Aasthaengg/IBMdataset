s =""
while True:
    try:
        s += input().lower()
    except:
        break
    
s = list(map(ord,list(s)))
for i in range(ord("a"),ord("z")+1):
    print(chr(i) + " : " + str(s.count(i)))