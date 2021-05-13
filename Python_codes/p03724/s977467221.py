#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n, m = map(int, input().split())
  counts = [0] * (n)
  for _ in range(m):
    a, b = map(int, input().split())
    counts[a-1] += 1
    counts[b-1] += 1
  if all([c%2==0 for c in counts]):
    print('YES')
  else:
    print('NO')

if __name__=='__main__':
  main()

