# import bisect
# from collections import Counter, defaultdict, deque, namedtuple
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
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
    a = list(map(int,ipti().split()))
    b = list(map(int,ipti().split()))

    a_sum = sum(a)
    b_sum = sum(b)

    if a_sum < b_sum:
        print(-1)
        sys.exit()

    a_minus_b = [a[i] - b[i] for i in range(n)]

    a_minus_b.sort()
    minus_count = 0
    minus_sum = 0

    for i in range(n):
        if a_minus_b[i] < 0:
            minus_count += 1
            minus_sum += -(a_minus_b[i])
        else:
            break

    plus_count = 0
    plus_sum = 0

    for i in range(n-1, -1, -1):
        plus_sum += a_minus_b[i]
        plus_count += 1
        if plus_sum >= minus_sum:
            break

    if minus_count == 0:
        print(0)
    else:
        print(plus_count+minus_count)



if __name__ == '__main__':
    main()