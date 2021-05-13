#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n = int(input())
  odd_count = sum([int(input()) % 2 for _ in range(n)])
  print('first' if odd_count > 0 else 'second')

if __name__=='__main__':
  main()

