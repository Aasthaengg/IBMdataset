#!/usr/bin/env python3

def calcExpectedValue(prob):
  return (prob+1)/2

def solve(n,k,p):
  expLst = [calcExpectedValue(prob) for prob in p]
  cum = [0]*(n+1)
  for i in range(n):
    cum[i+1] = cum[i] + expLst[i]
  ans = 0
  i = 0
  while i+k <= n:
    ans = max(ans,cum[i+k]-cum[i])
    i += 1
  return ans




def main():
  N,K = map(int,input().split())
  p = list(map(int,input().split()))
  print(solve(N,K,p))
  return

if __name__ == '__main__':
  main()
