n=int(input())
temp=100
ans=0
dp=list(list(map(int,input().split())) for i in range(n))

for i in range(1,n):
  dp[i][0]+=max(dp[i-1][1], dp[i-1][2])
  dp[i][1]+=max(dp[i-1][0], dp[i-1][2])
  dp[i][2]+=max(dp[i-1][1], dp[i-1][0])
print(max(dp[n-1]))