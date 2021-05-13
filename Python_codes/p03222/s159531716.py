fib = [None] * 11
fib[0], fib[1] = 1, 2
for i in range(2, 11):
    fib[i] = fib[i-1] + fib[i-2]
mod = 1000000007
H, W, K = map(int, input().split())
if W == 1:
    print(1)
    quit()
dp = [[0] * W for i in range(H+1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if 1 < j < W-2:
            dp[i+1][j] += dp[i][j] * fib[j-1] * fib[W-j-2] % mod
            dp[i+1][j] += dp[i][j-1] * fib[j-2] * fib[W-j-2] % mod
            dp[i+1][j] += dp[i][j+1] * fib[j-1] * fib[W-j-3] % mod
        elif j == 1:
            dp[i+1][j] += dp[i][j] * fib[j-1] * fib[W-j-2] % mod
            dp[i+1][j] += dp[i][j-1] * fib[W-j-2] % mod
            dp[i+1][j] += dp[i][j+1] * fib[j-1] * fib[W-j-3] % mod
        elif j == W-2:
            dp[i+1][j] += dp[i][j] * fib[j-1] * fib[W-j-2] % mod
            dp[i+1][j] += dp[i][j-1] * fib[j-2] * fib[W-j-2] % mod
            dp[i+1][j] += dp[i][j+1] * fib[j-1] % mod
        elif j == 0:
            dp[i+1][0] = dp[i][0] * fib[W-2] + dp[i][1] * fib[W-3]
        elif j == W-1:
            dp[i+1][W-1] = dp[i][W-1] * fib[W-2] + dp[i][W-2] * fib[W-3]
        dp[i+1][j] %= mod
print(dp[H][K-1])