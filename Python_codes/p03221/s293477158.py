import bisect
n,m=map(int,input().split())
a=dict()
b=[]
for i in range(m):
    p,y=map(int,input().split())
    b.append((p,y))
    if p not in a:
        a[p]=[y]
    else:
        a[p]+=[y]
for i,l in a.items():
    a[i]=sorted(l)
for p,y in b:
    index=bisect.bisect_left(a[p],y)+1
    a1=str(p).zfill(6)
    a2=str(index).zfill(6)
    print(a1+a2)
