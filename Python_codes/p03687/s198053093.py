#!/usr/bin/env python3

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

INF = pow(10,5)

def countProcedure(lst,char,cnt=0):
  flags = [x == char for x in lst]
  if all(flags):
    return cnt
  else:
    lst = [char if lst[i] == char or lst[i+1] == char else lst[i] for i in range(len(lst)-1)]
    return countProcedure(lst,char,cnt+1)

# @njit
def solve(s):
  s = list(s)
  res = INF
  for char in (chr(ord("a") + i) for i in range(26)):
    res = min(res,countProcedure(s,char))

  return res



def main():
  s = input()
  print(solve(s))
  return

if __name__ == '__main__':
  main()
