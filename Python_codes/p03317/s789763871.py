import sys

import bisect

# from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd

import itertools

# from operator import attrgetter, itemgetter
import math

# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, k = list(map(int, readline().split()))
    a = list(map(int, readline().split()))

    ans = 1
    rem = max(n - k, 0)
    ans += math.ceil(rem / (k - 1))

    print(ans)


if __name__ == '__main__':
    main()
