MOD = 10**9 + 7
H, W = map(int, input().split())
maze = []
for _ in range(H):
  maze.append(input())

dp = [[0]*W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
  for j in range(W):
    if i-1 >= 0 and maze[i][j] == ".":
      dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
    if j-1 >= 0 and maze[i][j] == ".":
      dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
print(dp[H-1][W-1])