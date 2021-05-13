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
    s = list(input())
    target = ["A", "B", "C"]
    next = ["B", "C"]

    idx = 0
    ans = 0
    a_cnt = 0

    while len(s) - 3 >= idx:
        if [s[idx], s[idx + 1], s[idx + 2]] == target:
            ans += a_cnt
            ans += 1
            a_cnt += 1

            idx += 3
            while len(s) - 3 >= idx:
                if [s[idx], s[idx + 1], s[idx + 2]] == target:
                    ans += a_cnt + 1
                    idx += 3
                    a_cnt += 1
                else:
                    break

            while len(s) - 2 >= idx:
                if [s[idx], s[idx + 1]] == next:
                    ans += a_cnt
                    idx += 2
                else:
                    break

        elif s[idx] != "A":
            a_cnt = 0
            idx += 1
        elif s[idx] == "A":
            a_cnt += 1
            idx += 1

    print(ans)


if __name__ == '__main__':
    main()
