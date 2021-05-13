import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
import bisect

if __name__ == "__main__":
    n = int(input())
    x = list(map(int,input().split()))
    y = x[:]
    y.sort()
    L = y[n//2-1]
    R = y[n//2]
    for i in range(n):
        if x[i] <= L:
            print(R)
        else:
            print(L)