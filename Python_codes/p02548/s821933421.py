import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += (n-1)//i
    print(ans)


if __name__ == '__main__':
    main()
