# -*- coding: utf-8 -*-

A,B,C = [int(i) for i in input().rstrip().split()]

max = B // A
if max < C:
  print(max)
else:
  print(C)
