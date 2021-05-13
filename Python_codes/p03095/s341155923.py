#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  MAX = 10**9 + 7
  counts = [0] * 26
  
  n = int(input())
  dp = [[0]*2 for _ in range(26)] 
  for c in list(input().strip()):
    counts[ord(c) - 97] += 1
    
  dp[0][0] = 1
  dp[0][1] = counts[0]
  for i, count in enumerate(counts[1:], 1):
    if count == 0:
      dp[i] = dp[i-1]
      continue
    dp[i][0] = sum(dp[i-1]) % MAX
    dp[i][1] = (dp[i][0] * counts[i]) % MAX
  
  print((sum(dp[-1]) - 1) % MAX)

if __name__=='__main__':
  main()

