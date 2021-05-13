#!/usr/bin/env python3
import sys
from fractions import gcd
import math

def main():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    tmp = 1
    count = None
    for i in range(N):
      tmp = (tmp * a[i]//2) // gcd(tmp,a[i]//2)
      c = 0
      n = a[i]//2
      while n % 2 == 0:
        c += 1
        n //= 2
      if i == 0:
        count = c
      elif count != c:
        print(0)
        exit()
    print((M//tmp +1)//2)

if __name__ == '__main__':
    main()
