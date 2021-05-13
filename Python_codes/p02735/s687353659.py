import math
h,w = map(int,input().split())
g = [list(input()) for _ in range(h)]
dp = [[float('inf')]*w for _ in range(h)]
if g[0][0] == '.':
    dp[0][0] = 0
else:
    dp[0][0] = 1

for i in range(h):
    for j in range(w):
        for di, dj in zip((0,1), (1, 0)):
            ni, nj = i+di, j+dj
            if ni>=h or nj>=w:
                continue
            if g[ni][nj]!=g[i][j]:
                dp[ni][nj] = min(dp[ni][nj], dp[i][j]+1)
            else:
                dp[ni][nj] = min(dp[ni][nj], dp[i][j])
print(math.ceil(dp[h-1][w-1]/2))