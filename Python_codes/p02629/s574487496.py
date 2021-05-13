#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n = int(input())
  d = 26
  name = ''
  while n > 0:
    if n % d == 0:
      name += chr(ord('a') - 1 + d)
      n -= d
    else:
      name += chr(n % d + ord('a') - 1 )
      n -= n % d
    n //= d
  print(name[::-1])

if __name__=='__main__':
  main()

