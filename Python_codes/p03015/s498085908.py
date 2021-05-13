l=input()
n=len(l)
mod=10**9+7
dp=[[0]*2 for i in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
  dp[i][1]+=dp[i-1][1]*3
  if l[i-1]=='1':
    dp[i][0]+=2*dp[i-1][0]
    dp[i][1]+=dp[i-1][0]
  else:
    dp[i][0]+=dp[i-1][0]
  dp[i][0]%=mod
  dp[i][1]%=mod
print((dp[i][0]+dp[i][1])%mod)