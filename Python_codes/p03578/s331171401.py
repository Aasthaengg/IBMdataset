import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions

import copy

# import heapq
# from collections import deque
# import decimal

sys.setrecursionlimit(10000001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    n = ni()
    d = na()
    m = ni()
    t = na()

    d_set = set(d)
    d_cnt = collections.Counter(d)

    for ti in t:
        if ti in d_set and d_cnt[ti] > 0:
            d_cnt[ti] -= 1
        else:
            print("NO")
            exit(0)

    print("YES")


if __name__ == '__main__':
    main()
