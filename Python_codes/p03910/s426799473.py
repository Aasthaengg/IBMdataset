import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal

sys.setrecursionlimit(10000001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===
def main():
    n = ni()
    d = []
    tmp = 0
    for i in range(10 ** 7):
        tmp += i
        d.append(tmp)
        if tmp > 10 ** 7 + 1000:
            break

    l = bisect.bisect_left(d, n)
    ans = []
    tmp_n = n
    for i in range(l, 0, -1):
        if tmp_n >= i:
            ans.append(i)
            tmp_n -= i

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
