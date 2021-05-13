#!/usr/bin/env python3

# from numba import njit
from collections import Counter

# input = stdin.readline

# @njit
def solve(n,l):
  l_dash = ["".join(sorted(s)) for s in l]
  d = Counter(l_dash)
  return sum(v*(v-1)//2 for v in d.values())


def main():
  N = int(input())
  l = [input() for _ in range(N)]
  print(solve(N,l))
  return

if __name__ == '__main__':
  main()
