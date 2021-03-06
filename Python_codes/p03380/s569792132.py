#!/usr/bin/env python3


def solve(n,a):
  a = list(sorted(a,reverse=True))
  first = a[0]
  b = a[1:]
  delta = [abs(x-first//2) for x in b]
  second = b[delta.index(min(delta))]
  return first,second

def main():
  N = int(input())
  a = list(map(int,input().split()))
  print(*solve(N,a))

if __name__ == '__main__':
  main()