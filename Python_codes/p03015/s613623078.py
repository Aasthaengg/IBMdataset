l=input()
mod=10**9+7

dp=[[0]*2 for i in range(len(l)+1)]
dp[0][0]=1

for i in range(len(l)):
  dp[i+1][1]+=(dp[i][1]*3)%mod

  if l[i]=='1':
    dp[i+1][0]+=(dp[i][0]*2)%mod
    dp[i+1][1]+=(dp[i][0])%mod
  
  else:
    dp[i+1][0]+=(dp[i][0])%mod


print((dp[-1][0]+dp[-1][1])%mod)