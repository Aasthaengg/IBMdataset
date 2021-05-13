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
import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, m = ns()
    matA = [list(input()) for _ in range(n)]
    matB = [list(input()) for _ in range(m)]

    a = np.array(matA)
    b = np.array(matB)

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if np.all(a[j:j + m, i:i + m] == b):
                print("Yes")
                exit(0)

    print("No")


if __name__ == '__main__':
    main()
