import sys

def S(): return sys.stdin.readline().rstrip()

H,W,K = map(int,S().split())
mod = 10**9+7

if W == 1:
    print(1)
    exit()

fib = [1,1,2,3,5,8,13,21]  # fib[i] = i本の縦線に横線を引く方法の数(同じ高さ)

dp = [[0]*(W+1) for _ in range(H+1)]  # dp[i][j] = i行目にjに達する横線の引き方

for i in range(H+1):
    for j in range(W+1):
        if i == 0:
            if j == 1:
                dp[i][j] = 1
        else:
            if j == 1:
                dp[i][j] = dp[i-1][j]*fib[W-1] + dp[i-1][j+1]*fib[W-2]
                dp[i][j] %= mod
            elif j == W:
                dp[i][j] = dp[i-1][j-1]*fib[W-2] + dp[i-1][j]*fib[W-1]
                dp[i][j] %= mod
            elif 2 <= j <= W-1:
                dp[i][j] = dp[i-1][j-1]*(fib[j-2]*fib[W-j]) + dp[i-1][j]*(fib[j-1]*fib[W-j]) + dp[i-1][j+1]*(fib[j-1]*fib[W-j-1])
                dp[i][j] %= mod

print(dp[H][K])