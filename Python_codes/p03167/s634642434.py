import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())
G = [readline().rstrip() for i in range(H)]
DIV = 10 ** 9 + 7

dp = [[0] * (W + 1) for i in range(H + 1)]
dp[0][1] = 1
for i in range(H):
  for j in range(W):
    if G[i][j] == "#":
      dp[i + 1][j + 1] = 0
      continue
    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]
    dp[i + 1][j + 1] %= DIV
    
print(dp[-1][-1])