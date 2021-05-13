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
    S = sum(A)
    X = [0 for _ in range(N)]

    for i in range(1, N, 2):
        X[0] -= 2 * A[i]
    X[0] += S

    for i in range(1, N):
        X[i] = 2 * A[i - 1] - X[i - 1]
    print(*X)


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
