import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n, m, q = map(int, readline().split())
lr = [list(map(int, readline().split())) for _ in range(m)]
cnt = [[0] * (n + 1) for _ in range(n + 1)]
for l, r in lr:
    cnt[l][r] += 1
cnt = np.cumsum(cnt, axis=0).cumsum(axis=1).tolist()
for _ in range(q):
    p, q = map(int, readline().split())
    p -= 1
    ans = cnt[q][q] + cnt[p][p]
    ans -= cnt[q][p] + cnt[p][q]
    print(ans)
