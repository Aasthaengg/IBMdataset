import numpy as np
from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))


@lru_cache(maxsize=None)
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


ans = a[0]

for i in a[1:]:
    ans = gcd(ans, i)

print(ans)