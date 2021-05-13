H, W = map(int, input().split())

A = ['' for i in range(H)]
dp = [[1 for i in range(W)] for j in range(H)]

for i in range(H):
  A[i] = input()

for i in range(0, H):
  for j in range(0, W):
    if i+j == 0:
      continue
    if A[i][j] == '#':
      dp[i][j] = 0
    else:
      if (A[i-1][j] == '#') or (i == 0): x=0
      else: x = dp[i-1][j]
      if (A[i][j-1] == '#') or (j == 0): y=0
      else: y = dp[i][j-1] 
      dp[i][j] = x+y

print(dp[-1][-1] % (10**9+7))