#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n = int(input())
  sb  = 0
  lab = [0] * n
  for i in range(n):
    a, b = map(int, input().split())
    sb += b
    lab[i] = a+b
  lab.sort(reverse=True)
  print(sum(lab[::2]) - sb)

if __name__=='__main__':
  main()

