# https://atcoder.jp/contests/abc138/tasks/abc138_e

from collections import defaultdict
from bisect import bisect_right

S = input()
T = input()

# Sの中での位置
iS = defaultdict(list)
for (idx, ch) in enumerate(S):
    iS[ch].append(idx)

# Tの文字はSに出ていないといけない
for v in T:
    if v not in iS:
        print(-1)
        exit()

# 探索
cnt = 0
cur = -1
for v in T:
    i = bisect_right(iS[v], cur)
    if i == len(iS[v]):
        j = iS[v][0]
    else:
        j = iS[v][i]

    if cur >= j:
        cnt += 1
    cur = j

print(cnt * len(S) + cur + 1)