#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  r, d, x = map(int, input().strip().split())
  for i in range(10):
    x = r*x - d
    print(x)

if __name__=='__main__':
  main()

