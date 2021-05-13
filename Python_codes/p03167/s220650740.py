H, W = map(int, input().split())

MOD = 10**9 + 7
dp = [[0]*W for _ in range(H)]

for i in range(H):
  grid = input()
  if i == 0:
    Flag = True
    for j in range(W):
      if grid[j] == "#":
        Flag = False
      if Flag:
        dp[i][j] = 1
      else:
        dp[i][j] = 0
  else:
    for j in range(W):
      if grid[j] == "#":
        dp[i][j] = 0
      else:
        if j == 0:
          dp[i][j] = dp[i-1][j]
        else:
          dp[i][j] = (dp[i-1][j] + dp[i][j-1])%MOD

print(dp[-1][-1])