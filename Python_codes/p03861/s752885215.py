# -*- coding : utf-8 -*-

a,b,x = map(int, input().split())

A = a // x
B = b // x
if a % x != 0:
  print(B-A)
else:
  print( B-A + 1)
