# -*- coding: utf-8 -*-
import math

#入力
#S = str(input())
#N, i = map(int, input().split())
#K = int(input())
A, B = map(int, input().split())

if B%A == 0 :
  print (A+B)
else :
  print (B-A)