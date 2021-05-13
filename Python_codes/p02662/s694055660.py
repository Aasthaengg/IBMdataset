n,s=map(int,input().split())
a=list(map(int,input().split()))
mod=998244353
dp=[[0]*(s+1) for i in range(n+1)]
dp[0][0]=pow(2,n,mod)
x=pow(2,mod-2,mod)
for i in range(n):
  for j in range(s+1):
    if j>=a[i]:
      dp[i+1][j]=(dp[i][j-a[i]]*x+dp[i][j])%mod
    else:
      dp[i+1][j]=dp[i][j]%mod
print(dp[n][s])