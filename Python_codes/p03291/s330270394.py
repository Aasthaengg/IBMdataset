#!/usr/bin/python3
# -*- coding: utf-8 -*-
MOD = 1000000007


def main():
  S = str(input())
  dp = [[0 for _ in range(3)] for _ in range(len(S)+1)]
  A,AB,ABC = [0,1,2]
  wc_num = 1
  for i,s in enumerate(S):
    if s in "A?":
      dp[i+1][A] = (dp[i+1][A]+dp[i][A]+wc_num) % MOD
      dp[i+1][AB] = (dp[i+1][AB]+dp[i][AB]) % MOD
      dp[i+1][ABC] = (dp[i+1][ABC]+dp[i][ABC]) % MOD
    if s in "B?":
      dp[i+1][A] = (dp[i+1][A]+dp[i][A]) % MOD
      dp[i+1][AB] = (dp[i+1][AB]+dp[i][AB]+dp[i][A]) % MOD
      dp[i+1][ABC] = (dp[i+1][ABC]+dp[i][ABC]) % MOD
    if s in "C?":
      dp[i+1][A] = (dp[i+1][A]+dp[i][A]) % MOD
      dp[i+1][AB] = (dp[i+1][AB]+dp[i][AB]) % MOD
      dp[i+1][ABC] = (dp[i+1][ABC]+dp[i][ABC]+dp[i][AB]) % MOD
    if s == "?":
      wc_num = (wc_num*3) % MOD
  print(dp[len(S)][ABC])



if __name__ == "__main__":
  main()