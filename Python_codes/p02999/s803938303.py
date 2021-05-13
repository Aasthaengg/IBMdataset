#!/usr/bin/env python

from sys import stdin, stderr

def main():
   X, A = map(int, stdin.readline().split())
   print(0 if X < A else 10)

   return 0

if __name__ == '__main__': main()
