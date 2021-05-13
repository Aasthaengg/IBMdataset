# -*- coding: utf-8 -*-
A, B = map(int, input().split())
if(B==0):
  print(A)
else:
  t = (A+B) % 24
  print(t)
