# -*- coding: utf-8 -*-

N,K = [int(i) for i in input().rstrip().split()]

if N%K == 0:
  print(0)
else:
  print(1)
