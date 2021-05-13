#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n = int(input())
  la = [int(input()) for _ in range(n)]
  cnt = 0
  
  if la[0] != 0:
    print(-1)
    return
  for i in range(n-1):
    if la[i+1] > la[i] + 1:
      print(-1)
      return
    
  for i in range(n)[::-1]:
    if i+1 < n and la[i]+1 == la[i+1]:
      continue
    else:
      cnt += la[i]
  print(cnt)
    
if __name__=='__main__':
  main()

