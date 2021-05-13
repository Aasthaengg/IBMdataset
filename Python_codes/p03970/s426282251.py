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
S = str(input())

cnt = 0
A = "CODEFESTIVAL2016"

for i in range(len(S)) :
  if S[i] != A[i] :
    cnt += 1
print (cnt)

