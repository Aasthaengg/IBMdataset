import sys
import numpy as np
H, W = map(int, input().split())
I = np.array([list(map(str, input())) for _ in range(H)])
grid = np.zeros([H,W], np.int16)
grid[np.where(I=='#')] = 1
inf = np.inf
dp = np.full([H,W], inf)
if grid[0,0] == 1:
    dp[0,0] = 1
else:
    dp[0,0] = 0

for i in range(H):
    for j in range(W):
        if i + 1 < H:
            if grid[i,j] == grid[i+1,j]:
                dp[i+1,j] = min(dp[i+1,j], dp[i,j])
            else:
                dp[i+1,j] = min(dp[i+1,j], dp[i,j]+1)
        if j + 1 < W:
            if grid[i,j] == grid[i,j+1]:
                dp[i,j+1] = min(dp[i,j+1], dp[i,j])
            else:
                dp[i,j+1] = min(dp[i,j+1],dp[i,j]+1)
if grid[-1,-1] == 1:
    dp[-1,-1,] += 1
ans = dp[-1,-1]//2
print(int(ans))
