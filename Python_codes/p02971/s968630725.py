l=[]
n=int(input())
for _ in range(n):
    a=int(input())
    l.append(a)
maxl=max(l)
a=l.count(maxl)
if a>=2:
    for _ in range(n):
        print(maxl)
else:
    for i in range(n):
        if l[i]!=maxl:
            print(maxl)
        else:
            ll=l.copy()
            l.remove(maxl)
            print(max(l))
            l=ll