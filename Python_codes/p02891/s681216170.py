#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

def countProcedure(string):
  res = 0
  strCount = 1
  prev = "" # 1つまえの文字
  for i in range(len(string)):
    if string[i] == prev:
      strCount += 1
    else:
      res += strCount // 2
      strCount = 1
    prev = string[i]

  if strCount != 1:
    res += strCount // 2
  return res

def solve(s,k):
  if s[0] != s[-1]:
    return countProcedure(s)*k
  if all(x == s[0] for x in s):
    return len(s)*k//2
  else:
    leftLength = max(i for i in range(1,len(s)) if s[:i]== s[0]*i)
    left = s[0]*leftLength
    right = s[leftLength:]
    ans = countProcedure(left) + countProcedure(right) + countProcedure("".join([right,left]))*(k-1)
    return ans


def main():
  S = input()
  K = int(input())
  # N,M = map(int,input().split())
  # a = list(map(int,input().split()))
  print(solve(S,K))
  
  
if __name__ == '__main__':
  main()
