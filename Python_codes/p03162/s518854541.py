import numpy as np

N = int(input())
a = np.zeros((N,3))
for i in range(N):
  a[i][0],a[i][1],a[i][2] = map(int,input().split())

ans = 0

# dpテーブル
dp = np.zeros((N+1,3))

for i in range(N):
  for x in range(3):
    for y in range(3):
      if x == y:
        continue
      dp[i+1][y] = max(dp[i+1][y],dp[i][x]+a[i][y])


print(int(max(dp[N][0],dp[N][1],dp[N][2])))