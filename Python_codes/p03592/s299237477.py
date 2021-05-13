import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions

import copy

# import heapq
# from collections import deque
# import decimal

sys.setrecursionlimit(10000001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    n, m, k = ns()

    for i in range(m + 1):
        for j in range(n + 1):
            if (m-i)*j+(n-j)*i==k:
                print("Yes")
                exit(0)

    print("No")


if __name__ == '__main__':
    main()
