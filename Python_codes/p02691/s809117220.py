#!/usr/bin/python3
# -*- coding:utf-8 -*-

from collections import defaultdict

def main():
  n = int(input())
  la = list(map(int, input().split()))
  cum = defaultdict(int)
  for i, a in enumerate(la, 1):
    cum[i - a] += 1
    
  cnt = 0
  for i, a in enumerate(la, 1):
    cnt += cum[a + i]
  print(cnt)

if __name__=='__main__':
  main()
