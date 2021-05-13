#!/usr/bin/python3
# -*- coding:utf-8 -*-

from collections import defaultdict

def main():
  n, t = map(int, input().split())
  la = list(map(int, input().split()))
  min_a = 10**9 + 7
  max_a = -1
  
  cnts = defaultdict(int)
  for a in la:
    min_a = min(min_a, a)
    cnts[a - min_a] += 1
  print(cnts[max(cnts.keys())])

if __name__=='__main__':
  main()

