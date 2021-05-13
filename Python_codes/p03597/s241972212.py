import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    n = int(input())
    a = int(input())

    print(n**2-a)


if __name__ == '__main__':
    main()
