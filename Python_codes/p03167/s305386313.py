mod = 10 ** 9 + 7

H, W = map(int, input().split())
A = [input() for _ in range(H)]

dp = [[0] * (W + 1) for _ in range(H + 1)]
dp[0][1] = 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        if A[i - 1][j - 1] == ".":
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(dp[H][W] % mod)