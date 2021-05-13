import sys
import math
import collections
import bisect
import itertools

import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    n = ni()
    a = na()
    b = a.copy()

    a_cnt = 0
    a_sum = 0
    b_cnt = 0
    b_sum = 0

    for i in range(n):
        tmp = a_sum + a[i]
        if i % 2:
            if tmp <= 0:
                a_cnt += 1 + abs(tmp)
                a_sum = 1
            else:
                a_sum += a[i]
        else:
            if tmp >= 0:
                a_cnt += 1 + abs(tmp)
                a_sum = -1
            else:
                a_sum += a[i]

    for i in range(n):
        tmp = b_sum + b[i]
        if not i % 2:
            if tmp <= 0:
                b_cnt += 1 + abs(tmp)
                b_sum = 1
            else:
                b_sum += b[i]
        else:
            if tmp >= 0:
                b_cnt += 1 + abs(tmp)
                b_sum = -1
            else:
                b_sum += b[i]

    print(min(a_cnt, b_cnt))


if __name__ == '__main__':
    main()
