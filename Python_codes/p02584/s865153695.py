#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  x, k, d = map(int, input().strip().split())
  x = abs(x)
  if x >= k * d:
    print(x - k * d)
  else:
    k -= (x // d)
    print(abs(x % d - (k % 2) * d))

if __name__=='__main__':
  main()

