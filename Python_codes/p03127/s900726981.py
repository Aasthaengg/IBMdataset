#!/usr/bin/env python3

# from numba import njit
from math import gcd
from functools import reduce
# input = stdin.readline

# @njit
def solve(n,a):
  ans = reduce(gcd,a)
  return ans



def main():
  N = int(input())
  # N,M = map(int,input().split())
  a = list(map(int,input().split()))
  print(solve(N,a))
  return

if __name__ == '__main__':
  main()
