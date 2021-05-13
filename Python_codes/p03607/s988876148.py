#!/usr/bin/env python3
from collections import Counter

def isOdd(x):
  return x % 2

def solve(n,a):
  d = Counter(a)
  return sum(map(isOdd,d.values()))


def main():
  N = int(input())
  a = [int(input()) for _ in range(N)]
  print(solve(N,a))
  return

if __name__ == '__main__':
  main()
