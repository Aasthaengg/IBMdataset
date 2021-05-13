#!/usr/bin/env python3

# from numba import njit
import sys
sys.setrecursionlimit(10**9)
# input = stdin.readline

INF = 10**9

# @njit
def solve(n):
  s = 0
  l = []
  for i in range(n):
    s += i+1
    l += [i+1]
    if s > n:
      l.remove(s-n)
      return l
    elif s == n:
      return l

  return -1



def main():
  N = int(input())
  # N,M = map(int,input().split())
  # a = list(map(int,input().split()))
  print(*solve(N),sep="\n")
  return

if __name__ == '__main__':
  main()
