#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline



# @njit
def solve(n,a,b):
  res = 0

  for i in range(n):
    res += (-a[i]-res) % b[i]

  return res



def main():
  N = int(input())
  a = [0]*N
  b = [0]*N
  for i in range(N):
    a[i],b[i] = map(int,input().split())
  print(solve(N,a[::-1],b[::-1]))
  return

if __name__ == '__main__':
  main()
