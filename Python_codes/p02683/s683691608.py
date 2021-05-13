n,m,x=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=[]
for i in range(2**n):
    bag=[0 for _ in range(m)]
    total=0
    res=True
    for j in range(n):
        if ((i>>j)&1):
            total+=a[j][0]
            for k in range(m):
                bag[k]+=a[j][k+1]
    for l in range(m):
        if bag[l]<x:
            res=False
            break
    if res:
        ans.append(total)

if ans!=[]:
    print(min(ans))
else:
    print(-1)
