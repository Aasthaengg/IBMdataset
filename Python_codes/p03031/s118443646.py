n,m=map(int, input().split())
k=[list(map(int, input().split())) for _ in range(m)]
p=list(map(int, input().split()))

ans=0

for i in range(2**n):
    t=0
    for j in range(m):
        o=sum(1 for h in k[j][1:] if i >>(h-1)&1)
        if o%2==p[j]:
            t+=1
    if t==m:
        ans+=1
print(ans)