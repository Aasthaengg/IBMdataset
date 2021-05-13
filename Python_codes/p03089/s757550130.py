import sys

# import re
import math
import collections
# import decimal
import bisect
# import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    a = na()

    ans = []
    while len(a) > 0:
        flg = True
        for i in range(len(a) - 1, -1, -1):
            if i + 1 == a[i]:
                ans.append(i + 1)
                del a[i]
                flg = False
                break
        if flg:
            print(-1)
            exit(0)

    for i in range(n-1,-1,-1) :
        print(ans[i])


if __name__ == '__main__':
    main()
