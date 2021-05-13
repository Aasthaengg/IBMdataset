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
N, A, B = map(int, input().split())

maxN = min(A, B)
minN = max(A+B-N, 0)

print (str(maxN) + " " + str(minN))