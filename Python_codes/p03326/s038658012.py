#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n, m = map(int, input().split())
  lxyz = [[0]*3 for _ in range(n)]
  for i in range(n):
    lxyz[i] = list(map(int, input().split()))
  
  def binary(x, k, t=1, f=0):
    return [t if (x >> ik)%2 else f for ik in range(k)]
  
  ans = -1
  for lh in [binary(i, 3, f=-1) for i in range(8)]:
    ans = max(ans, abs(sum(sorted([sum(map(lambda x: x[0]*x[1], zip(lh, lxyz[i]))) for i in range(n)], reverse=True)[:m]))) 
  print(ans)
  
if __name__=='__main__':
  main()

