#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n = input().strip()[::-1]
  dp = [[0, 0] for _ in range(len(n))]
  dp[0][0] = int(n[0])
  dp[0][1] = 10 - int(n[0])
  for i, d in enumerate(map(int, n[1:]), 1):
    dp[i][0] = min(dp[i-1][0] + d,      dp[i-1][1] + 1 + d)
    dp[i][1] = min(dp[i-1][0] + 10 - d, dp[i-1][1] + 10 - (d + 1))
  print(min(dp[-1][0], dp[-1][1]+1))  

if __name__=='__main__':
  main()

