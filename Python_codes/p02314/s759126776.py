n,m = map(int,input().split())
c = list(map(int,input().split()))
dp = [[10000000000]*m for _ in range(n+1)]
dp[0] = [0]*m

"""
m i 枚数
n j 金額

"""

for j in range(1,n+1):
  for i in range(m):
    v = c[i]
    if j >= v:
      dp[j][i] = min(dp[j][i-1],dp[j-v][i-1]+1,dp[j-v][i]+1)
    else:
      dp[j][i] = dp[j][i-1]
      
print(dp[n][m-1])
