s = input()
l = len(s)

alf=set('abcdefghijklmnopqrstuvwxyz')
for i in range(l):
    if s[i] in alf:
        alf.remove(s[i])

if alf:
    t = list(alf)
    t.sort()
    s+=t[0]
else:
    stock=[]
    for i in range(1,26):
        if s[l-i-1]>s[l-i]:
            stock.append(s[l-i])
        else:
            stock.append(s[l-i])
            stock.sort()
            for j in stock:
                if j>s[l-i-1]:
                    s=s[:l-i-1]+j
                    print(s)
                    exit()
        if i==25:
            print('-1')
            exit()
print(s)
