import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    w,a,b = map(int, input().split())

    if ((a+w)<b) or ((b+w)<a):
        print(min(abs(a+w-b), abs(b+w-a)))
    else:
        print(0)


if __name__ == '__main__':
    main()
