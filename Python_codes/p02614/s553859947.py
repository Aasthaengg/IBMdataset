#!/usr/bin/python3
# -*- coding:utf-8 -*-

import numpy
from copy import deepcopy

def binary(x, n):
  l = []
  for i in range(n):
    l.append(x%2==1)
    x //= 2
  return l

def main():
  h, w, k = map(int, input().strip().split())
  mat = numpy.array([[1 if c=='#' else 0 for c in input().strip()] for _ in range(h)])
  
  def f(mat, i, j):
    mat[binary(i, h)] = 0
    mat[:, binary(j, w)] = 0
    return mat.sum() == k
  
  cnt = 0
  for i in range(2 ** h):
    for j in range(2 ** w):
      if f(deepcopy(mat), i, j):
        cnt += 1
  print(cnt)
      
if __name__=='__main__':
  main()
