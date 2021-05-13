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
    s = list(input())

    l = len(s)
    ans = l // 2

    for i in range(97, 97 + 26):
        word = chr(i)
        cnt = 0
        tmp_max = -1
        for j in range(l):
            if s[j] != word:
                cnt += 1
            else:
                tmp_max = max(tmp_max, cnt)
                cnt = 0
        ans = min(ans, max(tmp_max, cnt))

    print(ans)


if __name__ == '__main__':
    main()
