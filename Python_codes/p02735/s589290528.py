# DP
# . -> # に変わる回数が反転が必要な回数
# その最小経路をDPで解く
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
dp = [[0]*W for _ in range(H)]

def cnt(i0, j0, i1, j1):
  if S[i0][j0] == "." and S[i1][j1] == "#":
    return 1
  else:
    return 0

for i in range(H):
  for j in range(W):
    if i == 0 and j == 0:
      dp[0][0] = 0 if S[0][0] == "." else 1
    elif i == 0:
      dp[i][j] = dp[i][j-1] + cnt(i, j-1, i, j)
    elif j == 0:
      dp[i][j] = dp[i-1][j] + cnt(i-1, j, i, j)
    else:
      dp[i][j] = min(dp[i][j-1] + cnt(i, j-1, i, j), dp[i-1][j] + cnt(i-1, j, i, j))

print(dp[H-1][W-1])
