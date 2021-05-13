mod = 10 ** 9 + 7
H, W = map(int, input().split())
S = []
for i in range(H):
  S.append(input())
dp = [[0 for j in range(W)] for i in range(H)]
dp[0][0] = 1
for i in range(H):
  for j in range(W):
    if i == 0:
      if j == 0:
        continue
      else:
        if S[i][j] == ".":
          dp[i][j] = dp[i][j-1]
    else:
      if S[i][j] == ".":
        if j == 0:
          dp[i][j] = dp[i-1][j]
        else:
          dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
print(dp[H-1][W-1])