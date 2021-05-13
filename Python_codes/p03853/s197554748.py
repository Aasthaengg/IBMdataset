import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    h,w = map(int, input().split())
    C = [input() for _ in range(h)]
    for i in range(h):
        for j in range(2):
            print(C[i])


if __name__ == '__main__':
    main()
