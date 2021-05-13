import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    a,b = map(int, input().split())

    print(math.ceil((a+b)/2))


if __name__ == '__main__':
    main()
