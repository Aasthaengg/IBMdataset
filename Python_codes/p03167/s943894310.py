H, W = map(int, input().split(' '))
a = [['0' for _ in range(W + 1)] for _ in range(H + 1)]
dp = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
for i in range(H):
  str_a = input()
  for j in range(W):
     a[i+1][j+1] = str_a[j]
i, j = 1, 1
while i <= H and a[i][1] == '.':
  dp[i][1] = 1
  i += 1
while j <= W and a[1][j] == '.':
  dp[1][j] = 1
  j += 1
for i in range(2, H + 1):
  for j in range(2, W + 1):
    if a[i][j] == '.':
      dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[H][W] % 1000000007)