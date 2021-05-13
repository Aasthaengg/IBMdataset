import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    n,k = map(int, input().split())
    L = list(map(int, input().split()))

    L.sort()
    L = L[::-1]
    print(sum(L[:k]))


if __name__ == '__main__':
    main()
