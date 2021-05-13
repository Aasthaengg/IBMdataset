MOD = 10 ** 9 + 7
H, W, K = map(int, input().split())

if W == 1:
    print(1)
    exit()

dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        dp[i][j] %= MOD
        here = dp[i][j]
        for d in range(2 ** (W - 1)):
            d = format(d, '0' + str(W - 1) + 'b')
            if not d.count('11'):
                if j == 0:
                    if d[j] == '1':
                        dp[i + 1][j + 1] += here
                    else:
                        dp[i + 1][j] += here
                elif j == W - 1:
                    if d[j - 1] == '1':
                        dp[i + 1][j - 1] += here
                    else:
                        dp[i + 1][j] += here
                else:
                    if d[j - 1] == '1':
                        dp[i + 1][j - 1] += here
                    elif d[j] == '1':
                        dp[i + 1][j + 1] += here
                    else:
                        dp[i + 1][j] += here

print(dp[H][K - 1] % MOD)
