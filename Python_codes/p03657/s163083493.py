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
    a, b = list(map(int,ipti().split()))

    if a % 3 == 0 or b % 3 == 0 or (a+b) % 3 == 0:
        print("Possible")
    else:
        print("Impossible")

if __name__ == '__main__':
    main()