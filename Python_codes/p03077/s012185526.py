#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

# @njit
def solve(n,l):
  return (n - 1)//min(l) + 5



def main():
  N = int(input())
  l = [int(input()) for _ in range(5)]
  print(solve(N,l))
  return

if __name__ == '__main__':
  main()
