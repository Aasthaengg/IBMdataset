#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

# @njit
def solve(a,b,x):
  def countDivisible(k,d):
    return k // d
  return countDivisible(b,x) - countDivisible(a-1,x)



def main():
  a,b,x = map(int,input().split())
  # a = list(map(int,input().split()))
  print(solve(a,b,x))
  return

if __name__ == '__main__':
  main()
