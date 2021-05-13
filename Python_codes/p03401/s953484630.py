import sys

# import bisect
# from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter

# import math

# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())
    a = [0] + list(map(int, readline().split())) + [0]
    cost = 0

    for i in range(n + 1):
        cost += abs(a[i + 1] - a[i])

    for j in range(1, n + 1):
        omit = abs(a[j] - a[j - 1]) + abs(a[j + 1] - a[j])
        new = abs(a[j + 1] - a[j - 1])
        print(cost - omit + new)


if __name__ == '__main__':
    main()
