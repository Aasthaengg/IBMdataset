dp=[0]*87
dp[0]=2
dp[1]=1
for i in range(2,87):
  dp[i]=dp[i-1]+dp[i-2]
N=int(input())
print(dp[N])