#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  MAX = 10**9 + 7
  
  n = int(input())
  lc = [int(input()) for _ in range(n)]
  dp = [0] * (n)
  
  last_is = [-1]*(2*10**5+1)
  dp[0] = 1
  last_is[lc[0]] = 0
  for i,c in enumerate(lc[1:], 1):
    last_i = last_is[c]
    dp[i] = dp[i-1]
    if last_i != -1 and last_i != i-1:
      dp[i] += dp[last_i]
      dp[i] %= MAX
    last_is[c] = i

  print(dp[-1])
  

if __name__=='__main__':
  main()

