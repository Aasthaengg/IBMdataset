#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n = int(input())
  def f(d, n):
    m = n // d
    return m * (m+1) * d // 2
  print(sum([f(d, n) for d in range(1, n+1)]))
  
if __name__=='__main__':
  main()
