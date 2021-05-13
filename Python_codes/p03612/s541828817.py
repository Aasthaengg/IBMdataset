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
    p = na()

    cnt = 0
    for i in range(1, n + 1):
        if i<n:
            if p[i - 1] == i:
                p[i - 1], p[i] = p[i], p[i - 1]
                cnt += 1
        else:
            if p[i - 1] == i:
                p[i - 1], p[i-2] = p[i-1], p[i - 2]
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
