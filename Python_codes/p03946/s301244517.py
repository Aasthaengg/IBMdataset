import sys
import math
import collections
import bisect
import itertools

# import numpy as np

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
    n, t = ns()
    a = na()

    res = dict()
    s_num = a[0]
    for i in range(1, n):
        tmp = a[i] - s_num
        if tmp > 0:
            if tmp in res.keys():
                res[tmp] += 1
            else:
                res[tmp] = 1

        s_num = min(s_num, a[i])

    print(res[max(res.keys())] if n != 1 else 0)


if __name__ == '__main__':
    main()
