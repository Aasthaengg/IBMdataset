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
tMOD = 998244353


def main():
    x = ni()

    cnt = 0
    total=0
    while total < x:
        cnt += 1
        total += cnt

    print(cnt)

if __name__ == '__main__':
    main()
