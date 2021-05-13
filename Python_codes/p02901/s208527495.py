import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
bit_cnt = 2 ** N # 箱は最大で12個
INF = 10 ** 10
dp = [INF] * bit_cnt
dp[0] = 0
for _ in range(M):
    price, b = lr()
    open = sum([2 ** (x-1) for x in lr()]) # 1と3の箱を開ける鍵なら101となる
    for j in range(bit_cnt):
        if dp[j|open] > dp[j] + price:
            dp[j|open] = dp[j] + price

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
# 解き直し08