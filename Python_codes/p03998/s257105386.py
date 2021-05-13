#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

# @njit
def solve(d,next="A"):
  while len(d[next]) != 0:
    next = d[next].pop(0)
  return next



def main():
  d = {}
  d["A"] = list(input().upper())
  d["B"] = list(input().upper())
  d["C"] = list(input().upper())
  print(solve(d))
  return

if __name__ == '__main__':
  main()
