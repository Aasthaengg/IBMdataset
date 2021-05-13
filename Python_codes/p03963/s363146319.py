import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    n,k = map(int, input().split())

    print(k*(k-1)**(n-1))

if __name__ == '__main__':
    main()
