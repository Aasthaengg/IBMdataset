n = int(input())

dp = [[0]*16 for i in range(n)]
for j in range(16):
  dp[1][j] = 1

for i in range(2,n):
  for j in range(16):
    k = j//4
    dp[i][j] = dp[i-1][k]+dp[i-1][k+4]+dp[i-1][k+8]+dp[i-1][k+12]
    if j == 1:
      dp[i][j] -= dp[i-1][8]
    elif j == 6:
      dp[i][j] -= dp[i-1][1]
    elif j == 9:
      dp[i][j] -= dp[i-1][2]+dp[i-2][2]+dp[i-2][3]
    elif j == 13:
      dp[i][j] -= dp[i-2][2]
    else:
      continue

count = 0
for j in range(16):
  count += dp[n-1][j]

print(count%1000000007)