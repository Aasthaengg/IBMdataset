import sys
from functools import lru_cache

sys.setrecursionlimit(1000000000)

MOD = 10 ** 9 + 7

@lru_cache(maxsize=None)
def r(k, smaller):
    global s

    if k == len(s):
        return 1

    if smaller:
        if s[k] == "1":
            return (2 * r(k + 1, True) + r(k + 1, False)) % MOD
        else:
            return r(k + 1, True) % MOD
    else:
        return (3 * r(k + 1, False)) % MOD


s = input()
print(r(0, True))
