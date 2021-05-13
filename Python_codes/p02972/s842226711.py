# -*- coding: utf-8 -*-
import sys
import math
import os
import itertools
import string
import heapq
import _collections
from collections import Counter
from collections import defaultdict
from collections import deque
from functools import lru_cache
import bisect
import re
import queue
import decimal


class Scanner():
    @staticmethod
    def int():
        return int(sys.stdin.readline().rstrip())

    @staticmethod
    def string():
        return sys.stdin.readline().rstrip()

    @staticmethod
    def map_int():
        return [int(x) for x in Scanner.string().split()]

    @staticmethod
    def string_list(n):
        return [Scanner.string() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [Scanner.int() for i in range(n)]


MOD = int(1e09) + 7
INF = int(1e15)


def solve():
    N = Scanner.int()
    A = Scanner.map_int()
    A = [0] + A
    B = [0 for _ in range(N + 1)]
    for i in reversed(range(1, N + 1)):
        j = i
        t = 0
        while j < N + 1:
            t += B[j]
            j += i
        if A[i] != t % 2:
            B[i] = 1
    ans = sum(B)
    print(ans)
    if ans > 0:
        print(*[i for i, b in enumerate(B) if b == 1], sep=' ')


def main():
    # sys.setrecursionlimit(1000000)
    # sys.stdin = open("sample.txt")
    # T = Scanner.int()
    # for _ in range(T):
    #     solve()
    # print('YNeos'[not solve()::2])
    solve()


if __name__ == "__main__":
    main()
