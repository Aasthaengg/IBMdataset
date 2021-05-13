import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    x,t = map(int, input().split())

    print(max(0, x-t))


if __name__ == '__main__':
    main()
