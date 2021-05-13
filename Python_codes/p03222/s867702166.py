H, W, K = map(int, input().split())
mod = 10 ** 9 + 7
dp = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
dp[0][1] = 1

fib = [0] * (W + 1)
fib[1] = 1
for i in range(2, W + 1):
    fib[i] = fib[i - 1] + fib[i - 2]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        dp[i][j] = (dp[i - 1][j - 1] * fib[j - 1] * fib[W - j + 1] +
                    dp[i - 1][j] * fib[j] * fib[W - j + 1] +
                    dp[i - 1][j + 1] * fib[j] * fib[W - j]) % mod
print(dp[H][K])
