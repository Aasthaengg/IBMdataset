H, W, K = map(int, input().split())
mod = 10**9 + 7

dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1


def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)


for i in range(1, H+1):
    for j in range(W):
        left = j
        right = W - j - 1

        dp[i][j] = dp[i-1][j] * fib(left) * fib(right)

        if j > 0:
            dp[i][j] += dp[i-1][j-1] * fib(left-1) * fib(right)

        if j < W-1:
            dp[i][j] += dp[i-1][j+1] * fib(left) * fib(right - 1)

        dp[i][j] %= mod

print(dp[-1][K-1])