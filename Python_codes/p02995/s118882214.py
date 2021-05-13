#!/usr/bin/env python3

from math import gcd

def lcm(x,y):
  return x*y//gcd(x,y)

def solve(a,b,c,d):
  def countNonDivisor(n,c,d):
    return n - n//c - n//d + n//lcm(c,d)
  return countNonDivisor(b,c,d) - countNonDivisor(a-1,c,d)



def main():
  a,b,c,d = map(int,input().split())
  print(solve(a,b,c,d))

  return

if __name__ == '__main__':
  main()
