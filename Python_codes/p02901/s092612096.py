n,m=map(int,input().split())
g=(1<<n)
dp=[10**18]*g
dp[0]=0
for i in  range(m):
    a,s=map(int,input().split())
    f=0
    for k in map(int,input().split()):
        f+=1<<(k-1)
    for j in range(g-1,-1,-1):
        dp[j|f]=min(dp[j]+a,dp[j|f])
print(-1 if dp[-1]==10**18 else dp[-1])