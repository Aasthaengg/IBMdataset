S = input()
N = list(map(int,S))
L = len(N)

dp = [[0]*2 for i in [0]*(L+1)]
dp[0][1] = 1

for i in range(L):
    n = N[i]
    dp[i+1][0] = min(dp[i][0] + n, dp[i][1] + 10-n)
    if n == 9:
        dp[i+1][1] = dp[i][1]
    else:
        dp[i+1][1] = min(dp[i][0] + n + 1, dp[i][1] + 10 - (n+1))

print(dp[L][0])


