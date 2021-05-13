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
    s = list(sys.stdin.readline())
    del s[len(s) - 1]
    cnt = 0

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            cnt += 1

    print(max(0, cnt))


if __name__ == '__main__':
    main()
