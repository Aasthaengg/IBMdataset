import sys

# import re
import math
import collections
# import decimal
# import bisect
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

    b = [0 for i in range(n)]
    ans = []

    for i in range(n // 2, n):
        if a[i] == 1:
            b[i] = a[i]
            ans.append(i + 1)

    for i in range(n // 2 - 1, -1, -1):
        cnt = 0
        for j in range(i * 2 + 1, n, i + 1):
            cnt ^= b[j]
        if cnt != a[i]:
            b[i] = 1
            ans.append(i + 1)

    tmp = len(ans)
    print(tmp)
    if tmp > 0:
        print(*ans, sep=" ")


if __name__ == '__main__':
    main()
