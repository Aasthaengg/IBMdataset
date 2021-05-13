H,W = map(int,input().split())
MOD = 10 ** 9 + 7

grid = [""] * H
for i in range(H):
  grid[i] = input()
  
dp = [[0] * W for i in range(H)]
dp[0][0] = 1
for i in range(H):
  for j in range(W):
    if i + 1 < H and grid[i + 1][j] != "#":
      dp[i + 1][j] += dp[i][j]
      dp[i + 1][j] %= MOD
    if j + 1 < W and grid[i][j + 1] != "#":
      dp[i][j + 1] += dp[i][j]
      dp[i][j + 1] %= MOD
      
print(dp[-1][-1])