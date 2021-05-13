s=int(input())
if s<3:
  print(0)
  exit()
  
dp=[0]*(s+1)
dp[0]=1

for i in range(3,s+1):
  dp[i]=dp[i-1]+dp[i-3]
print((dp[s-1]+dp[s-3]) % (10**9+7))