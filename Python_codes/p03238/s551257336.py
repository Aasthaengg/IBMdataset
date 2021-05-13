# -*- coding: utf-8 -*-

n = int(input().strip())

if n ==1:
  print("Hello World")
else:
  A,B = [int(input().strip()) for _ in range(2)]
  print(A+B)