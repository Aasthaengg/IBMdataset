import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
import bisect

if __name__ == "__main__":
    n,m = map(int,input().split())
    if n == 1 and m == 1:
        print(1)
    elif n == 1:
        print(m-2)
    elif m == 1:
        print(n-2)
    else:
        print((n-2)*(m-2))