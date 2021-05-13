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
s = str(input())

cflag = False
for i in range(len(s)) :
  if s[i] == "C" :
    cflag = True
  if cflag == True and s[i] == "F" :
    print ("Yes")
    exit()
print ("No")
