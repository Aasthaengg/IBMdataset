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
L = list(map(int, input().split()))
L.sort()
if L[0] == 1 and L[1] == 4 and L[2] == 7 and L[3] == 9 :
  print ("YES")
else :
  print ("NO")