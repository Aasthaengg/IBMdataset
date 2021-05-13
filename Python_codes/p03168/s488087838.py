import sys
sys.setrecursionlimit(4000)

n = int(input())
p = [float(x) for x in input().split()]

dp = [[0]*(n+1) for i in range(n)]

dp[0][0] = 1-p[0]
dp[0][1] = p[0]

for i in range(n-1):
  for j in range(i+2):
    dp[i+1][j] += dp[i][j]*(1-p[i+1])
    dp[i+1][j+1] += dp[i][j]*p[i+1]

ans = 0
for i in range(n//2+1, n+1):
  ans += dp[n-1][i]
print(ans)