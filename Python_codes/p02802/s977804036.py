n,m=map(int,input().split())
li=[0]*n
ok=0
ng=0
pro=set()
for i in range(m):
    p,s=map(str,input().split())
    p=int(p)
    if s=="WA":
        li[p-1]+=1
    else:
        if not p in pro:
            ok+=1
            ng+=li[p-1]
            pro.add(p)
print(ok,ng)