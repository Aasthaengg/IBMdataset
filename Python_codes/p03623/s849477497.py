# -*- coding: utf-8 -*-
import math

#入力
x, a, b = map(int, input().split())
#N = str(input())

if abs(a-x) > abs(b-x) :
  print ("B")
else :
  print ("A")
