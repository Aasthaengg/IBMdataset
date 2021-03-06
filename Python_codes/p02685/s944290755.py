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
import heapq
import decimal
# import statistics
import queue
import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
# MOD = 10 ** 9 + 7
MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    def fast_pow(num, kata, mod):
        if kata == 0:
            return 1

        res = 1
        while kata > 0:
            if kata & 1 == 1:
                res = res * num % mod
            num = num * num % mod

            kata >>= 1
        return res

    def prepare(n, MOD):
        f = 1
        factorials = [1]
        for m in range(1, n + 1):
            f *= m
            f %= MOD
            factorials.append(f)
        inv = pow(f, MOD - 2, MOD)
        invs = [1] * (n + 1)
        invs[n] = inv
        for m in range(n, 1, -1):
            inv *= m
            inv %= MOD
            invs[m - 1] = inv
        return factorials, invs

    n, m, k = ns()

    p, i = prepare(n, MOD)

    result = 0

    for ki in range(k + 1):
        ans = 1
        ans *= m % MOD
        ans *= fast_pow(m - 1, n - 1 - ki, MOD)
        ans %= MOD
        ans *= p[n - 1] * i[ki] * i[n - 1 - ki]
        ans %= MOD

        result += ans
        result %= MOD

    print(result)


if __name__ == '__main__':
    main()
