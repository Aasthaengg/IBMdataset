MOD = 1000000007

H, W = map(int, input().split())
A = [input() for _ in range(H)]

dp = [[0 for j in range(W)] for i in range(H)]
dp[0][0] = 1

for i in range(1, H):
    if A[i][0] == '.':
        dp[i][0] = dp[i - 1][0]

for j in range(1, W):
    if A[0][j] == '.':
        dp[0][j] = dp[0][j - 1]

for i in range(1, H):
    for j in range(1, W):
        if A[i][j] == '.':
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            dp[i][j] %= MOD

print(dp[H - 1][W - 1])