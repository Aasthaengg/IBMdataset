import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    r = int(input())
    g = int(input())

    print(g*2-r)


if __name__ == '__main__':
    main()
