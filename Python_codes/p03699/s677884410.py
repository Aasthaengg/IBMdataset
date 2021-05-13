#!/usr/bin/env python3

def solve(n,s):
  s_sorted = sorted(s)
  s_sum = sum(s)
  if s_sum % 10 != 0:
    return s_sum
  for a in s_sorted:
    if  a % 10 != 0:
      return s_sum - a
  return 0



def main():
  N = int(input())
  s = [int(input()) for _ in range(N)]
  print(solve(N,s))
  return

if __name__ == '__main__':
  main()
