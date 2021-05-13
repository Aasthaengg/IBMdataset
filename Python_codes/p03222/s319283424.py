H, W, K = map(int, input().split())
MOD = 10 ** 9 + 7

if W == 1:
  print(1)
  exit()

root = []
for i in range(2 ** (W - 1)):
  flag = 1
  for j in range(1, W - 1):
    if ((i >> j) & 1) & (i >> (j - 1) & 1):
      flag = 0
      break
  if flag:
    root.append(i)

swap = [[j for j in range(W)] for _ in range(len(root))]
for i in range(len(root)):
  for j in range(W - 1):
    if (root[i] >> j) & 1:
      swap[i][j], swap[i][j + 1] =  swap[i][j + 1], swap[i][j]
#for i in range(len(root)):
#  print(swap[i])
  
dp = [[0 for _ in range(W)] for _ in range(H + 1)]
dp[0][0] = 1

for i in range(H):
  for s in swap:
    for j in range(W):
      dp[i + 1][s[j]] = (dp[i + 1][s[j]] + dp[i][j]) % MOD
#for i in range(H + 1):
#  print(dp[i])

print(dp[-1][K - 1])