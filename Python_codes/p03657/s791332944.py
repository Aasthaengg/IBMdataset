# -*- coding: utf-8 -*-

A,B = [int(i) for i in input().rstrip().split()]

if (A%3) == 0:
  print("Possible")
elif  (B%3) == 0:
  print("Possible")
elif  ((A+B)%3) == 0:
  print("Possible")
else:
  print("Impossible")