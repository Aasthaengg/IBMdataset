H,W = map(int,input().split())

grid = [None] * H

for i in range(H):
    grid[i] = input()

dp = [[0] * (W+1) for i in range(H+1)]

dp[1][1] = 1
M = 10 ** 9 + 7

for L in range(1,H + 1):
    for C in range(1,W + 1):
        if L == 1 and C == 1:
            continue
        else:
            if grid[L-1][C-1] == ".":
                dp[L][C] = dp[L][C-1] + dp[L-1][C]
                dp[L][C] %= M

print(dp[H][W])
