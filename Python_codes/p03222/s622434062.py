import sys
input = sys.stdin.readline
H, W, K = map(int, input().split())
mod = 10 ** 9 + 7
dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1
for i in range(H):
  for j in range(W):
    for b in range(pow(2, W - 1)):
      f = 0
      t = 0
      bb = []
      for k in range(W - 2, -1, -1):
        bb.append(int(b >= pow(2, k)))
        if b >= pow(2, k): b -= pow(2, k)
      for k in range(len(bb) - 1):
        if bb[k] and (bb[k + 1]):
          f = 1
          break
      if f: continue
      #print(bb, i)
      if j > 0:
        if bb[j - 1]:
          dp[i + 1][j - 1] += dp[i][j]
          dp[i + 1][j - 1] %= mod
          f = 1
      if j < W - 1:
        if bb[j]:
          dp[i + 1][j + 1] += dp[i][j]
          dp[i + 1][j + 1] %= mod
          f = 1
      if f == 0:
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= mod
print(dp[-1][K - 1])