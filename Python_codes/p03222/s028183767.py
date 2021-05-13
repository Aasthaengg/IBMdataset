import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

H,W,K = MI()
mod = 10**9+7

if W == 1:
    print(1)
    exit()

fib = [1,1,2,3,5,8,13,21]  # fib[i] = i本のあみだくじの、ある列に横線を引く方法の数

dp = [[0]*(W+1) for _ in range(H+1)]  # dp[i][j] = i段横線を引いたときに1からKに至るような横線の引き方
dp[0][1] = 1
for i in range(1,H+1):
    for j in range(1,W+1):
        if j == 1:
            dp[i][j] = dp[i-1][j+1]*fib[W-j-1] + dp[i-1][j]*fib[W-j]
            dp[i][j] %= mod
        elif j == W:
            dp[i][j] = dp[i-1][j-1]*fib[j-2] + dp[i-1][j]*fib[j-1]
            dp[i][j] %= mod
        else:
            dp[i][j] = dp[i-1][j-1]*fib[j-2]*fib[W-j] + dp[i-1][j+1]*fib[j-1]*fib[W-j-1] + dp[i-1][j]*fib[W-j]*fib[j-1]
            dp[i][j] %= mod

print(dp[H][K])
