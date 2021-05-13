import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
INF = 10**18


if __name__ == "__main__":
    l,r,d = map(int,input().split())
    ans = 0
    for i in range(l,r+1):
        if i%d == 0:
            ans+=1
    print(ans)