# coding: utf-8
import sys
from bisect import bisect_left
import itertools

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
    answer = INF
    for s, t in itertools.product(S[si-1:si+1], T[ti-1:ti+1]):
        temp = min(abs(s-x), abs(t-x)) + abs(s-t)
        if temp < answer:
            answer = temp
    print(answer)
# 
