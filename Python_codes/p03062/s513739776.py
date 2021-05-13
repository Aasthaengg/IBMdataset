n=int(input())
a=list(map(int,input().split()))
dp=[[0 for _ in range(2)] for _ in range(n+1)]
dp[0][1] = - 10**9
for i in range(n):
  dp[i+1][0]=max(dp[i][0]+a[i],dp[i][1]-a[i])
  dp[i+1][1]=max(dp[i][0]-a[i],dp[i][1]+a[i])
print(dp[n][0])