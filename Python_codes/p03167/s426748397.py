mod = 10**9+7
h,w = map(int,input().split())
grid = [[l == "#" for l in list(input())] for _ in range(h)]
dp = [[0]*w for _ in range(h)]
dp[0][0] = 1
for s in range(1,h+w):
  for i in range(max(0,s-w+1),min(h,s+1)):
    j = s-i
    if grid[i][j]:
      continue
    if i == 0:
      dp[i][j] = dp[i][j-1]
    elif j == 0:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = (dp[i][j-1]+dp[i-1][j])%mod
print(dp[-1][-1]%mod)