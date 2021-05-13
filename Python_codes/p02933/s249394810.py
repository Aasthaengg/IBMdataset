#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  a = int(input())
  s = input().strip()
  print(s if a >= 3200 else 'red')

if __name__=='__main__':
  main()

