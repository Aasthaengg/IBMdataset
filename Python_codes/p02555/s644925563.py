s=int(input())
if s<6:
  print(int(s>2))
  exit()
dp=[0]*(s+1)
dp[3]=1
dp[4]=1
dp[5]=1
for i in range(6,s+1):
  dp[i]=dp[i-1]+dp[i-3]
print(dp[s]%(10**9+7))