n,m=map(int,input().split())
d=[0 for i in range(m)]
for i in range(n):
    k=list(map(int,input().split()))
    for i in range(len(k)-1):
        d[k[i+1]-1]+=1
ans=0
for i in d:
    if i==n:
        ans+=1
print(ans)