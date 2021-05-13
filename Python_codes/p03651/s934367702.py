#!/usr/bin/python3
# -*- coding:utf-8 -*-

from functools import reduce

def calc_gcd(a, b):
  if a > b:
    a, b = b, a
  while b % a:
    a, b = b % a, a
  return a

def main():
  n, k = map(int, input().split())
  la = list(map(int, input().split()))
  if max(la) >= k and k % (reduce(calc_gcd, la)) == 0:
    print('POSSIBLE')
  else:
    print('IMPOSSIBLE')
  
if __name__=='__main__':
  main()

