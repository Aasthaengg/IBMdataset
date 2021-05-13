#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline
MOD = 10**9+7
# @njit
def solve(n,stairs):
  # ～段目と対応
  dp = [1] + [0] * (n+1)
  dp[1] = stairs[1]
  for i in range(n):
    dp[i+2] = (dp[i] + dp[i+1]) * stairs[i+2]
    dp[i+2] %= MOD

  return dp[n]



def main():
  N,M = map(int,input().split())
  stairs = [1]*(N+10)
  for i in range(M):
    stairs[int(input())] = 0
  print(solve(N,stairs))
  return

if __name__ == '__main__':
  main()
