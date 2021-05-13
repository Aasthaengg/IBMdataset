import sys
import re
import math
import collections
import decimal
import bisect
import itertools

import copy

# import heapq
# from collections import deque
# import decimal

# sys.setrecursionlimit(100001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    s = list(input())

    w_cnt = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == "W":
            ans += i - w_cnt
            w_cnt += 1
    print(ans)


if __name__ == '__main__':
    main()
