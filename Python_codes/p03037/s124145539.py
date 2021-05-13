n,m=map(int,input().split())
l,r=[],[]
for i in range(m):
    a,b=map(int,input().split())
    l.append(a)
    r.append(b)
s=0
t=n+1
for i in range(m):
    if l[i]>s:
        s=l[i]
    if r[i]<t:
        t=r[i]
if s>t:
    print(0)
else:
    print(t-s+1)