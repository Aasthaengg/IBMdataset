# -*- coding: utf-8 -*-
 
import math
import itertools
import sys
import copy
 
# 入力
X, Y = map(int, input().split())
#A = int(input())
#B = int(input())

if X%Y == 0 :
  print (-1)
else :
  i = 2
  while (True) :
    if X*i % Y != 0 :
      print (X*i)
      break
    i += 1
