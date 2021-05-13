#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n, m = map(int, input().split())
  la, lb = [], []
  lc = []
  MAX = 10**9
  dp = [MAX] * (2 ** 13)
  dp[0] = 0
  
  for _ in range(m):
    a, b = map(int, input().split())
    la.append(a)
    lb.append(b)
    lc.append(sum([1 << c for c in map(int, input().split())]))
    
  for a, c in zip(la, lc):
    for ic in range(len(dp)):
      dp[c | ic] = min(a + dp[ic], dp[c | ic])
  if dp[2**(n+1)-2] != MAX:
    print(dp[2**(n+1)-2])
  else:
    print(-1)

if __name__=='__main__':
  main()

