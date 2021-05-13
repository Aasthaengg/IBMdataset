h, w, k = map(int, input().split())
k -= 1
MOD = 10 ** 9 + 7

valid_connections = []
for i in range(2 ** (w - 1)):
    if '11' not in bin(i):
        valid_connections.append(i)

dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        for connection in valid_connections:
            if connection & (1 << j):
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
            elif connection & (1 << max(j - 1, 0)):
                dp[i + 1][j - 1] += dp[i][j]
                dp[i + 1][j - 1] %= MOD
            else:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD

print(dp[h][k])