import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())
G = [None] * (H + 1)
G[0] = "." * (W + 1)
for i in range(H):
  G[i + 1] = "." + readline().rstrip()

dp = [[0] * (W + 1) for i in range(H + 1)]
dp[1][0] = 1 # 便宜上、枠外に1を入れておくことで、dp[1][1]が1になる
DIV = 10 ** 9 + 7

for i in range(1, H + 1):
  for j in range(1, W + 1):
    if G[i][j] == "#":
      dp[i][j] = 0
    else:
      dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
      dp[i][j] %= DIV
      
print(dp[H][W])