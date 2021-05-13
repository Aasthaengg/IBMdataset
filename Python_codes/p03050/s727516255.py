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

    ans = 0
    for i in range(1, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            diff = n // i - n // (i + 1) - 1
            if diff * i >= i:
                ans += n // i - 1
    print(ans)


if __name__ == '__main__':
    main()
