#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n = int(input())
  la = list(map(int, input().split()))
  lb = list(map(int, input().split()))
  lc = list(map(int, input().split()))
  la.sort(), lb.sort(), lc.sort()
  
  i = 0
  ab = []
  for b in lb:
    while i < n and la[i] < b:
      i += 1
    ab.append(i)
      
  i = 0
  bc = []
  for c in lc:
    while i < n and lb[i] < c:
      i += 1
    bc.append(i)
    
  ans = 0
  cs = [0]
  for x in ab:
    cs.append(cs[-1] + x)
  for y in bc:
    ans += cs[y]
  print(ans)
  

if __name__=='__main__':
  main()

