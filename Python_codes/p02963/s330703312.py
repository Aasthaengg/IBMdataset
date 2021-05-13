#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  s = int(input())
  remain   = - s % (10**9) % (10**9)
  quotient = (s + remain) // (10**9)
  print(0, 0, 1, 10**9, quotient, remain)
  
if __name__=='__main__':
  main()

