# import bisect
# from collections import Counter, defaultdict, deque, namedtuple
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

def main():
    n = int(input())
    b = list(map(int,ipti().split()))

    res = [0] * n

    for i in range(1, n + 1):
        for j in range(n - i, -1, -1):
            if b[j] == j + 1:
                res[n-i] = b.pop(j)
                break
        else:
            print(-1)
            sys.exit()

    for i in range(n):
        print(res[i])




if __name__ == '__main__':
    main()