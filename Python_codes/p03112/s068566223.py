# coding: utf-8
import sys
from bisect import bisect_left

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 番兵を左右に置いて、4通り試す
A, B, Q = lr()
INF = 10 ** 12
S = [-INF] + [ir() for _ in range(A)] + [INF]
T = [-INF] + [ir() for _ in range(B)] + [INF]
S.sort(); T.sort()
for _ in range(Q):
    x = ir()
    si = bisect_left(S, x)
    ti = bisect_left(T, x)
    temp = []
    temp.append(max(S[si], T[ti]) - x)
    y = abs(S[si] - x)
    z = abs(T[ti-1] - x)
    temp.append(min(y, z) * 2 + max(y, z))
    y = abs(S[si-1] - x)
    z = abs(T[ti] - x)
    temp.append(min(y, z) * 2 + max(y, z))
    temp.append(x - min(S[si-1], T[ti-1]))
    print(min(temp))

# 46
