import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# dfs, dp, bit全探索
# 箱が12個以下
N, M = lr()
keys = [None] * M
for i in range(M):
    a, b = lr()
    C = lr()
    bit = 0
    for c in C:
        bit += 1 << (c-1)
    keys[i] = (a, bit)

INF = 10 ** 9
dp = [INF] * 2 ** N # 2**N - 1 が全ての箱を開けられる状態の最小値
dp[0] = 0
for key in keys:
    a, bit = key
    for i in range(2 ** N):
        dp[i|bit] = min(dp[i|bit], dp[i] + a)

print(-1 if dp[-1] == INF else dp[-1])
