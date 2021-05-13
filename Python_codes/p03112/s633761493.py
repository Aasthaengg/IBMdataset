from functools import lru_cache
from bisect import bisect
from sys import stdin
input = stdin.readline
A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]

@lru_cache(maxsize=None)
def func(f, x):
    L = S if f else T
    i = bisect(L, x)
    if i == 0:
        return abs(x - L[0])
    elif i == len(L):
        return abs(x - L[-1])
    else:
        return min(abs(x - L[i]), abs(x - L[i - 1]))

for x in [int(input()) for _ in range(Q)]:
    ans = float("inf")
    i = bisect(S, x)
    if i != 0:
        ans = min(ans, func(0, S[i - 1]) + x - S[i - 1])
    if i != A:
        ans = min(ans, func(0, S[i]) + S[i] - x)
    i = bisect(T, x)
    if i != 0:
        ans = min(ans, func(1, T[i - 1]) + x - T[i - 1])
    if i != B:
        ans = min(ans, func(1, T[i]) + T[i] - x)
    print(ans)