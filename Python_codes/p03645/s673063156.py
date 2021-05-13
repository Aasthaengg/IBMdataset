#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**9)

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

# @njit
def solve(n,m,l):
  edges = {i+1:[] for i in range(n)}
  for i in range(m):
    a,b = l[i]
    edges[a].append(b)
    edges[b].append(a)
  return any(1 in v and n in v for k,v in edges.items())



def main():
  N,M = map(int,input().split())
  l = [tuple(map(int,input().split())) for _ in range(M)]
  print("POSSIBLE" if solve(N,M,l) else "IMPOSSIBLE")
  return

if __name__ == '__main__':
  main()
