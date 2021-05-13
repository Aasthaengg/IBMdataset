r,c=map(int,input().split())
q=range
b=[]
for i in q(r):
    w=[int(i) for i in input().split()]
    w.append(sum(w))
    b.append(w)
    print(*w)
l=[]
for i in q(c+1):
    x=0
    for a in b:x+=a[i]
    l.append(x)
print(*l)