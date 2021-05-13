import sys
H, W = map(int, input().split())
S = [list(s.rstrip()) for s in sys.stdin.readlines()]
dp = [[10**9] * W for _ in range(H)]
if S[0][0] == '#':
  dp[0][0] = 1
else:
  dp[0][0] = 0
for h in range(H):
  for w in range(W):
    for a, b in ((h+1, w), (h, w+1)):
      if a >= H or b >= W:
        continue
      else:
        if S[h][w] == '.' and S[a][b] == '#':
          dp[a][b] = min(dp[a][b], dp[h][w]+1)
        else:
          dp[a][b] = min(dp[a][b], dp[h][w])
print(dp[H-1][W-1])