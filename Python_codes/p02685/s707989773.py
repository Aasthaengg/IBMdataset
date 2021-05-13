#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  MAX = 998244353
  n, m, k = map(int, input().split())
    
  cnt = 0
  cmb = 1
  for ik in range(k+1):
    ncp = m * pow(m-1, n-ik-1, MAX)
    ncp %= MAX
    
    if ik == 0:
      cmb = 1
    else:
      cmb *= ((n-ik) * pow(ik, MAX-2, MAX))
    cmb %= MAX
    
    cnt += ncp * cmb
    cnt %= MAX
    
  print(cnt % MAX)

if __name__=='__main__':
  main()

