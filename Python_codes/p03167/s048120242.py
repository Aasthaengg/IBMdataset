MOD = 10**9+7

H, W = map(int, input().split())
dp = []
grid = []

for _ in range(H):
    dp.append([0] * W)
    grid.append(input())

dp[0][0] = 1

for r in range(H):
    for c in range(W):
        if grid[r][c] == "#" or (r == 0 and c == 0):
            continue

        up = dp[r-1][c] if r > 0 else 0
        left = dp[r][c-1] if c > 0 else 0

        dp[r][c] = (up + left) % MOD

print(dp[-1][-1])


