import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    W = input()

    c = collections.Counter(W)
    for key in c.keys():
        if c[key] % 2 != 0:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    main()
