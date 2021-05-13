s=input()
n=len(s)
mod=10**9+7
dp=[[0]*2 for _ in range(n)]
dp[0][0]=2
dp[0][1]=1
for i in range(n-1):
  d=int(s[i+1])
  dp[i+1][1]=(3*dp[i][1]+d*dp[i][0])%mod
  dp[i+1][0]=(dp[i][0]+d*dp[i][0])%mod
print(sum(dp[-1])%mod)