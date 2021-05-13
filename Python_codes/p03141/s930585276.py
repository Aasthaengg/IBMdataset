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

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    d = []
    for _ in range(n):
        a, b = ns()
        d.append((a + b, a, b))

    d.sort(reverse=True)
    turn = 1
    taka = 0
    ao = 0
    for i in range(n):
        if turn:
            taka += d[i][1]
        else:
            ao += d[i][2]
        turn ^= 1
    print(taka - ao)


if __name__ == '__main__':
    main()
