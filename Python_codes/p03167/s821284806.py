MOD = 1000000007
H, W = (int(x) for x in input().split())
grid = []
for row in range(H):
  grid.append(input())
# Number of paths to get to end grid[i][j]
dp = [[0 for i in range(W)] for i in range(H)]
# dp[H-1][W-1] == '#' ? 1 : return 0
if grid[H-1][W-1] == '#':
  print(0)
else:
  dp[H-1][W-1] = 1

for i in range(W-2, -1, -1):
  if grid[H-1][i] == '#':
    dp[H-1][i] = 0
    continue
  dp[H-1][i] = dp[H-1][i+1]
for i in range(H-2, -1, -1):
  if grid[i][W-1] == '#':
    dp[i][W-1] = 0
    continue
  dp[i][W-1] = (dp[i+1][W-1]) % MOD

for i in range(H-2, -1, -1):
  for j in range(W-2, -1, -1):
    if grid[i][j] == '#':
      dp[i][j] = 0
    else:
      dp[i][j] = (dp[i+1][j] + dp[i][j+1]) % MOD
print(dp[0][0])