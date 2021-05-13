# import bisect
# from collections import Counter, defaultdict, deque
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
    r = int(input())

    if r < 1200:
        print("ABC")
    elif r < 2800:
        print("ARC")
    else:
        print("AGC")

if __name__ == '__main__':
    main()