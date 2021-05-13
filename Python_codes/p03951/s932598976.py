#!/usr/bin/env python3

def solve(n,s,t):
  for i in range(n+1):
    if s[i:] == t[:n-i]:
      return len(s[:i]) + n
  return 2*n


def main():
  N = int(input())
  s = input()
  t = input()
  print(solve(N,s,t))
  return

if __name__ == '__main__':
  main()
