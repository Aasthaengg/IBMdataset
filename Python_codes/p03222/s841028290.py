MOD = 10 ** 9 + 7
H, W, K = map(int, input().split())

if W == 1:
    print(1)
    exit()

pat = [0] * W
for i in range(2 ** (W - 1)):
    j = bin(i)
    if not str(j).count('11'):
        pat[len(j) - 2] += 1
for i in range(W - 1):
    pat[i + 1] += pat[i]
pat[0] = 1

dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        k = j + 1
        if k == 1:
            dp[i + 1][j] += dp[i][j] * pat[max(0, W - 1 - 1)]
            dp[i + 1][j] += dp[i][j + 1] * pat[max(0, W - 1 - 2)]
        elif 1 < k < W:
            dp[i + 1][j] += dp[i][j] * pat[max(0, j - 1)] * pat[max(0, W - k - 1)]
            dp[i + 1][j] += dp[i][j - 1] * pat[max(0, j - 2)] * pat[max(0, W - k - 1)]
            dp[i + 1][j] += dp[i][j + 1] * pat[max(0, j - 1)] * pat[max(0, W - k - 2)]
        else:
            dp[i + 1][j] += dp[i][j] * pat[max(0, W - 1 - 1)]
            dp[i + 1][j] += dp[i][j - 1] * pat[max(0, W - 1 - 2)]

        dp[i+ 1][j] %= MOD

print(dp[H][K - 1])
