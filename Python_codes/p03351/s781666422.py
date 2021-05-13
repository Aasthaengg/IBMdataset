# -*- coding: utf-8 -*-
 
import math
import itertools
import sys
import copy
 
# 入力
#A, B, C, D = map(int, input().split())
#L = list(map(int, input().split()))
#S = list(str(input()))
#N = int(input())
#S = str(input())
a, b, c, d = map(int, input().split())

if abs(a-c) <= d :
  print ("Yes")
  exit()
else :
  if abs(a-b) <= d and abs(b-c) <= d :
    print ("Yes")
    exit()
print ("No")

