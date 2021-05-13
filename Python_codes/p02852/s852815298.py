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
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, m = ns()
    s = list(input())

    ans = []

    idx = n
    while idx != 0:
        exitFlg = True
        for i in range(min(idx, m), 0, -1):
            if s[idx - i] == "0":
                idx -= i
                ans.append(i)
                exitFlg=False
                break

        if exitFlg:
            print(-1)
            exit(0)

    ans.reverse()
    print(*ans, sep=" ")


if __name__ == '__main__':
    main()
