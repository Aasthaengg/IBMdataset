import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    n = int(input())
    for i in range(8):
        if 2**i > n:
            print(2**(i-1))
            return


if __name__ == '__main__':
    main()
