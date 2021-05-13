n,m,x=map(int,input().split())
cc=[list(map(int,input().split())) for _ in range(n)]
ans=float('inf')
for b in range(1<<n):
    a=[0]*(m+1)
    for i in range(n):
        if b&(1<<i)==0:
            continue
        for k,l in enumerate(cc[i]):
            a[k]+=l
        if min(a[1:])>=x:
            ans=min(ans,a[0])
    a=[0]*(m+1)
if ans==float('inf'):
    print(-1)
else:
    print(ans)
        
