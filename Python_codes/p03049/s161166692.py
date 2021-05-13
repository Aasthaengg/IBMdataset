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
    b_start = 0
    a_end = 0
    b_and_a = 0
    ans = 0

    for _ in range(n):
        s = input()
        ans += s.count("AB")
        flgB = s[0] == "B"
        flgA = s[-1] == "A"
        if flgB and flgA:
            b_and_a += 1
        elif flgB:
            b_start += 1
        elif flgA:
            a_end += 1

    remain_a = max(0, a_end - b_and_a)
    remain_b = max(0, b_start - b_and_a)
    remain_ab_a = max(0, b_and_a - b_start)
    remain_ab_b = max(0, b_and_a - a_end)

    ans += min(b_start, b_and_a)
    ans += min(a_end, b_and_a)
    ans += min(remain_a, remain_b)

    if remain_ab_a == remain_ab_b == b_and_a:
        if min(remain_ab_a, remain_ab_b) > 0:
            ans += min(remain_ab_a, remain_ab_b) - 1
    else:
        ans += min(remain_ab_a, remain_ab_b)

    print(ans)


if __name__ == '__main__':
    main()
