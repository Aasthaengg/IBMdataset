import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    k = ni()
    a = na()
    a.reverse()

    min_num = 2
    max_num = 2

    for ai in a:
        min_num = int(math.ceil(min_num / ai) * ai)
        max_num = int(math.floor(max_num / ai + 1) * ai) - 1

    if min_num <= max_num:
        print(min_num, max_num)
    else:
        print(-1)


if __name__ == '__main__':
    main()
