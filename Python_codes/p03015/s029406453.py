L = input()
N = len(L)

mod = 10**9 + 7

dp = [[0]*(N+1) for _ in range(2)]
dp[1][0] = 1

for i in range(1, N+1):
    c = L[i-1]
    if c == '1':
        dp[1][i] = 2*dp[1][i-1] % mod
        dp[0][i] = (3*dp[0][i-1] + dp[1][i-1]) % mod
    else:
        dp[1][i] = dp[1][i-1]
        dp[0][i] = 3*dp[0][i-1] % mod

print((dp[0][-1] + dp[1][-1]) % mod)
