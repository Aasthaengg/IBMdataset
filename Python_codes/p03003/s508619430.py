N, M = map(int, input().split())
s_list = list(map(int, input().split()))
t_list = list(map(int, input().split()))
mod = 10 ** 9 + 7
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if s_list[i - 1] == t_list[j - 1]:
            dp[i][j] += dp[i - 1][j - 1] + 1
            dp[i][j] %= mod
        dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        dp[i][j] %= mod
print((dp[N][M] + 1) % mod)
