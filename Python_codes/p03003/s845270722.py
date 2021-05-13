import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
N, M = lr()
S = [0] + lr()
T = [0] + lr()
dp = [[0] * (M+1) for _ in range(N+1)]
dp_cum = [[0] * (M+1) for _ in range(N+1)]
dp[0][0] = 1; dp_cum[0][0] = 1
for i in range(N+1):
    dp_cum[i][0] = 1
for j in range(M+1):
    dp_cum[0][j] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        if S[i] == T[j]:
            dp[i][j] = dp_cum[i-1][j-1]
        else:
            dp[i][j] = 0
        dp_cum[i][j] = (dp_cum[i-1][j] + dp_cum[i][j-1] - dp_cum[i-1][j-1] + dp[i][j]) % MOD

answer = dp_cum[N][M]
print(answer)
# 02