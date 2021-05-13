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

N = int(input())
S = str(input())

r = 0
b = 0
for i in range(N) :
  if S[i] == "R" :
    r += 1
  else :
    b += 1

if r > b :
  print ("Yes")
else :
  print ("No")
  

