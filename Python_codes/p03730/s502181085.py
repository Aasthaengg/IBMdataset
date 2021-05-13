#!/usr/bin/env python3

from math import gcd

def solve(a,b,c):
  d = gcd(a,b)
  if c % d == 0:
    return "YES"
  else:
    return "NO"



def main():
  a,b,c = map(int,input().split())
  print(solve(a,b,c))
  return

if __name__ == '__main__':
  main()
