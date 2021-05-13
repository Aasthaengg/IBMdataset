n,s=map(int,input().split())
dp=[0]*(s+1)
dp[0]=1
ne=[0]*(s+1)
mod=998244353
for i in list(map(int,input().split())):

    for k in range(0,s+1):
        if k+i<=s:
            ne[k+i]=(ne[k+i]+dp[k])%mod
        ne[k]=(ne[k]+2*dp[k])%mod
        dp[k]=0
    dp,ne=ne,dp
print(dp[-1])