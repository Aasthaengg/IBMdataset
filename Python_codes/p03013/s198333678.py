#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline
MOD = 10**9+7
# @njit
def solve(n,a):
  # ～段目と対応
  stairs = [1]*(n+10)
  for x in a:
    stairs[x] = 0

  dp = [1] + [0] * (n+1)
  dp[1] = stairs[1]
  for i in range(n):
    dp[i+2] = (dp[i] + dp[i+1]) * stairs[i+2]
    dp[i+2] %= MOD

  return dp[n]



def main():
  N,M = map(int,input().split())
  a = [int(input()) for _ in range(M)]
  print(solve(N,a))
  return

if __name__ == '__main__':
  main()
