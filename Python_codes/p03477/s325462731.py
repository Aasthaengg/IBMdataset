# -*- coding: utf-8 -*-
import math

#入力
#C1 = str(input())
#C2 = str(input())
A, B, C, D = map(int, input().split())

if (A+B) > (C+D) :
  print ("Left")
elif (A+B) < (C+D) :
  print ("Right")
else :
  print ("Balanced")