# -*- coding: utf-8 -*-
 
import math
import itertools
import sys
import copy
 
# 入力
#X, Y = map(int, input().split())
N = str(input())

cnt = 0
for i in range(4) :
  if N[i] == "2" :
    cnt += 1
print (cnt)