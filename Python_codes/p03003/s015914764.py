import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
N, M = lr()
S = ['?'] + lr()
T = ['.'] +lr()
# dp[i][j] はSがi文字目までTがj文字目までの部分列で等しい組の総和
dp = [[1] * (M+1) for _ in range(N+1)]

for j in range(1, M+1):
    for i in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        if S[i] == T[j]:
            dp[i][j] += (dp[i-1][j-1])
        dp[i][j] %= MOD

answer = dp[N][M]
print(answer%MOD)
# 21 pypy