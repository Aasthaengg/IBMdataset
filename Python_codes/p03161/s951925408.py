import sys
import numpy as np
# inputを高速化する。
input = sys.stdin.readline
n, k = map(int, input().split())
h = [int(i) for i in input().split()]
# dpの配列を作る。
dp = np.zeros(n, dtype=int)
# hの配列を作る。
h = np.array(h)
for i in range(1, n):
    # start は負になることはない。
    start = max(0, i-k)
    # 行列として足し算できるのでforを使う必要がない。
    dp[i] = min(dp[start: i] + np.abs(h[i] - h[start: i]))
print(dp[n-1])