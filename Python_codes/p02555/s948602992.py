from functools import lru_cache
import sys

sys.setrecursionlimit(2000)
mod = 10 ** 9 + 7

@lru_cache(maxsize=None)
def dp(i):
    if i == 1 or i == 2:
        return 0
    elif i == 3 or i == 4:
        return 1
    else:
        return (dp(i - 3) + dp(i - 1)) % mod


S = int(input())
print(dp(S))
