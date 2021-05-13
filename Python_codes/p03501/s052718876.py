import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    n,a,b = map(int, input().split())

    print(min(a*n, b))


if __name__ == '__main__':
    main()
