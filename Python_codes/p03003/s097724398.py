# 解説AC
from collections import defaultdict

N,M = map(int, input().split())
S = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]

MOD = 10 ** 9 + 7

# dp[i][j]: S[:i]とT[:j]での共通部分列の個数
dp = [[0] * (M + 1) for _ in range(N + 1)]

# 初期条件
for i in range(N + 1):
    dp[i][0] = 1
for j in range(M + 1):
    dp[0][j] = 1

# 貰うDP
for i, s in enumerate(S):
    for j, t in enumerate(T):
        dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]

        if s == t:
            dp[i + 1][j + 1] += dp[i][j]
        
        # ダブルカウントを除く
        dp[i + 1][j + 1] -= dp[i][j]

        dp[i + 1][j + 1] %= MOD

print(dp[N][M])