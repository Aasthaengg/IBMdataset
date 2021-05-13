h, w = list(map(int, input().split()))
m = 1000000007

grid = [input() for _ in range(h)]

dp = [[0 for _ in range(w)] for _ in range(h)]
dp[0][0] = 1

for y in range(h):
    for x in range(w):
        if grid[y][x] == ".":
            if y > 0:
                dp[y][x] += dp[y-1][x]
            if x > 0:
                dp[y][x] += dp[y][x-1]

            dp[y][x] %= m

print(dp[h-1][w-1])