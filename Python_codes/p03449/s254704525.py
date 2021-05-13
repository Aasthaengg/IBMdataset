import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
import bisect

if __name__  == "__main__":
    n = int(input())
    A1 = list(map(int,input().split()))
    A2 = list(map(int,input().split()))
    ruiseki_wa = [0]*(n)
    ruiseki_wa[0] = A1[0]
    for i in range(1,n):
        ruiseki_wa[i] = ruiseki_wa[i-1] + A1[i]
    ans = 0
    for i in range(n):
        c = ruiseki_wa[i]
        for j in range(i,n):
            c += A2[j]
        ans = max(ans,c)
    print(ans)