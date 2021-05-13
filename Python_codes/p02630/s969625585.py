#!/usr/bin/python3
# -*- coding:utf-8 -*-

from collections import defaultdict

def main():
  n = int(input())
  la = list(map(int, input().strip().split()))
  q = int(input())
  counts = defaultdict(int)
  for a in la:
    counts[a] += 1
  s = sum(la)
  for _ in range(q):
    b, c = map(int, input().strip().split())
    s -= b * counts[b]
    s += c * counts[b]
    print(s)
    
    counts[c] += counts[b]
    counts[b] = 0
    

if __name__=='__main__':
  main()

