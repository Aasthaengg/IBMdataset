h, w = map(int, input().split())
maze = [list(input()) for i in range(h)]
mod = 10 ** 9 + 7

dp = [[0] * (w + 1) for i in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if i == j == 1:
            dp[i][j] = 1
        elif maze[i - 1][j - 1] == ".":
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

print(dp[h][w])
