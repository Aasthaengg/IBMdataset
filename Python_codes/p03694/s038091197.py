import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    n = int(input())
    A = list(map(int, input().split()))

    A.sort()
    print(A[-1] - A[0])


if __name__ == '__main__':
    main()
