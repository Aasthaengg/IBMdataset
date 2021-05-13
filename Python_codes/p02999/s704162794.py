#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  x, a = map(int, input().strip().split())
  print(0 if x < a else 10)

if __name__=='__main__':
  main()

