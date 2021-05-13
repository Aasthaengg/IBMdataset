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
    A =[0] +  list(map(int,input().split())) + [0]
    prf = [0]
    for i in range(1,n+2):
        d = abs(A[i] - A[i-1])
        prf.append(prf[i-1] + d)
    for i in range(1,n+1):
        ans = prf[-1] - abs(A[i] - A[i-1]) - abs(A[i+1] - A[i]) + abs(A[i+1]-A[i-1])
        print(ans)