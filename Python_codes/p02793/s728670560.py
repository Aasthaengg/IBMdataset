import sys
# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    from functools import reduce

    n = ni()
    a = na()

    lcm = a[0]
    for i in a:
        lcm = lcm // math.gcd(lcm, i) * i
    lcm %= MOD

    ans = 0
    for ai in a:
        ans += lcm * pow(ai, MOD - 2, MOD) % MOD
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
