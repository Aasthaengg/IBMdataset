MOD = 10**9 + 7
H, W = map(int, input().split())
G = [input() for _ in range(H)]

dp = [[0] * W for _ in range(H)]
for i in range(H):
    if G[i][0] == '#':
        break
    dp[i][0] = 1
for i in range(W):
    if G[0][i] == '#':
        break
    dp[0][i] = 1


for i in range(1, H):
    for j in range(1, W):
        if G[i][j] == '#':
            dp[i][j] = 0
        else:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

print(dp[H - 1][W - 1])