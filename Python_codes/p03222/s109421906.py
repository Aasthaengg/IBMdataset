H, W, K = map(int, input().split())

dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1

B = [format(i, 'b').zfill(W - 1) for i in range(2 ** (W - 1)) if '11' not in format(i, 'b')]

for h in range(H):
  for w in range(W):
    for b in B:
      if w > 0 and b[w - 1] == '1':
      	dp[h + 1][w - 1] += dp[h][w]
      elif w < W - 1 and b[w] == '1':
        dp[h + 1][w + 1] += dp[h][w]
      else:
        dp[h + 1][w] += dp[h][w]

print(dp[H][K - 1] % (10**9 + 7))