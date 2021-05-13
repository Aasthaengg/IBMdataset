#!/usr/bin/python3
# -*- coding:utf-8 -*-

from math import ceil, floor

def main():
  k = int(input())
  la = list(map(int, input().split()))[::-1]
  l = 2
  r = 2
  for a in la:
    if ceil(l/a) > floor(r/a):
      print(-1)
      return
    l = ceil(l/a) * a
    r = floor(r/a) * a + a - 1
  print(l, r)
      

if __name__=='__main__':
  main()

