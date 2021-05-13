import sys


INF = sys.maxsize
H, W = map(int, input().split())
m = []

for i in range(H):
  m.append([x for x in input()])

dp = [[INF] * W for _ in range(H)]
dp[0][0] = 0 if m[0][0] == '.' else 1

for i in range(H):
  for j in range(W):    
    for di, dj in [(0, 1), (1, 0)]:
      ni = i + di
      nj = j + dj
      if ni < H and nj < W:
        dp[ni][nj] = min(
          dp[ni][nj],
          dp[i][j] + 1 if m[i][j] == '.' and m[ni][nj] == '#' else dp[i][j],
        )

print(dp[-1][-1])        