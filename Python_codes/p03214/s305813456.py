# -*- coding: utf-8 -*-
 
import math
import itertools
import sys
import copy
 
# 入力
#A, B, C, D = map(int, input().split())
#L = list(map(int, input().split()))
#S = list(str(input()))
N = int(input())
#S = str(input())
a = list(map(int, input().split()))

ave = 0
for i in range(N) :
  ave += a[i]
ave /= N

index = 0
absX = sys.maxsize
for i in range(N) :
  if absX > abs(ave - a[i]) :
    absX = abs(ave - a[i])
    index = i
    
print (index)
