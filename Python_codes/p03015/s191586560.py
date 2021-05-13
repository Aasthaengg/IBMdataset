L = input()
n = len(L)
mod = 10**9 + 7

dp = [[0]*2 for _ in range(n+1)]
#dp[i][flag]は、i桁目までみたときにflag = 1はストリクトにLより小さい
dp[0][0] = 1

for i in range(n):
    if L[i] == "1":
        dp[i+1][0] = 2*dp[i][0] % mod
        dp[i+1][1] = (3*dp[i][1] % mod + dp[i][0]) % mod
    else:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = 3*dp[i][1] % mod
print((dp[n][0]+dp[n][1]) % mod)