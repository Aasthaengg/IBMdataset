import sys
from functools import lru_cache


sys.setrecursionlimit(500000)


@lru_cache(maxsize=None)
def rec(n):
    if n == 0:
        return 0
    res = n
    i = 1
    while i <= n:
        res = min(res, rec(n - i) + 1)
        i *= 6
    i = 9
    while i <= n:
        res = min(res, rec(n - i) + 1)
        i *= 9
    return res


N = int(input())
print(rec(N))


