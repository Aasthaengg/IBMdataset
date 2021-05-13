n,c=map(int,input().split())
d=[[0]*c for _ in [0]*int(1e5)]
for _ in range(n):
    s,t,c=map(int,input().split())
    for j in range(s-1,t):
        d[j][c-1]=1

ans=1
for i in range(int(1e5)):
    s=sum(d[i])
    if s>ans:
        ans=s

print(ans)