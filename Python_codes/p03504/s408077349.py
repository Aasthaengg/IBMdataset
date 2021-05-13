#!/usr/bin/python3
# -*- coding:utf-8 -*-

import numpy

def main():
  n, c = map(int, input().split())
  recoders = numpy.zeros((c, 2*(10**5+1)), dtype=numpy.int)
  for _ in range(n):
    s, t, c = map(int, input().split())
    s = 2*s - 1
    t = 2*t
    c -= 1
    recoders[c][s:t] = 1
  
  print(max(numpy.sum(recoders, axis=0)))
    

if __name__=='__main__':
  main()

