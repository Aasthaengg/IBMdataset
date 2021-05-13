#!/usr/bin/env python3

# from numba import njit
from math import gcd
# input = stdin.readline

def lcm(x,y):
  return x*y//gcd(x,y)

# @njit
def solve(n,m,s,t):
  L = lcm(n,m)
  G = gcd(n,m)
  s_interval = L//n
  t_interval = L//m
  for i in range(G):
    if s[i*n//G] != t[i*m//G]:
      return -1
  return L
  

def main():
  N,M = map(int,input().split())
  s = input()
  t = input()
  print(solve(N,M,s,t))
  return

if __name__ == '__main__':
  main()
