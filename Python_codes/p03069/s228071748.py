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

    white, black = 0, 1
    s = [int(i) for i in list(input().replace(".", "0").replace("#", "1"))]
    s.insert(0, 0)
    black_total = s.count(1)

    cnt = [0, 0]  # [white,black]
    ans = INF
    for i in range(n, -1, -1):
        ans = min(ans, black_total - cnt[black] + cnt[white])
        cnt[s[i]] += 1

    print(ans)


if __name__ == '__main__':
    main()
