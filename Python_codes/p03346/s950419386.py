#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n = int(input())
  lp = [int(input()) for _ in range(n)]
  ilp = sorted(enumerate(lp), key=lambda x:x[1])
  max_cnt = 0
  cnt = 1
  for i in range(n-1):
    if ilp[i] < ilp[i+1]:
      cnt += 1
    else:
      max_cnt = max(max_cnt, cnt)
      cnt = 1
  print(n - max(max_cnt, cnt))
  
if __name__=='__main__':
  main()

