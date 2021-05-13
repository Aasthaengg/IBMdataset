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
    s = input()
    c = collections.Counter(s)

    l = len(s)
    total = l * (l - 1) // 2

    for ci in c.values():
        tmp = ci * (ci - 1) // 2
        total -= tmp

    print(total + 1)


if __name__ == '__main__':
    main()
