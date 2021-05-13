h, w = map(int, input().split())
S = [input() for _ in range(h)]
dp = [[0]*w for _ in range(h)]
for i in range(h):
  for j in range(w):
    if i == 0 and j == 0:
      if S[0][0] == "#":
        dp[0][0] = 1
      continue
    if i:
      u = dp[i-1][j]
      if S[i-1][j] == "." and S[i][j] == "#":
        u += 1
    else:
      u = float("inf")
    if j:
      v = dp[i][j-1]
      if S[i][j-1] == "." and S[i][j] == "#":
        v += 1
    else:
      v = float("inf")
    dp[i][j] = min(u, v)
print(dp[-1][-1])