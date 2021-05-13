n,m=map(int,input().split())
INF=10**10
dp=[[INF]*(1<<n) for _ in range(m+1)]
for i in range(m+1):
    dp[i][0]=0
a=[0]
key=[0]
for i in range(m):
    a0,b=map(int,input().split())
    a.append(a0)
    *c,=map(int,input().split())
    tmp=0
    for j in c:
        tmp+=1<<(j-1)
    key.append(tmp)

for i in range(1,m+1):
    for j in range(1<<n):
        if dp[i-1][j]<INF:
            dp[i][j]=min(dp[i][j],dp[i-1][j])
            dp[i][j|key[i]]=min(dp[i][j|key[i]],dp[i-1][j|key[i]],dp[i-1][j]+a[i])

ans=dp[-1][-1]
if ans!=INF:
    print(ans)
else:print(-1)
