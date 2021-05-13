import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy


if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(1,2*n,2):
        ans += a[i]
    print(ans)