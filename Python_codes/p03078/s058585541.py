import sys

import bisect

# from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd

import itertools

# from operator import attrgetter, itemgetter
# import math

# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x, y, z, k = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))
    c = list(map(int, readline().split()))

    ab = [0] * x * y

    ab = [i + j for i, j in itertools.product(a, b)]
    ab.sort(reverse=True)
    c.sort(reverse=True)

    ab = ab[:k]

    abc = [i + j for i, j in itertools.product(ab, c)]
    abc.sort(reverse=True)

    print(*abc[:k],sep="\n")

if __name__ == '__main__':
    main()
