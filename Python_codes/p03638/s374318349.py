# coding:utf-8

import sys
import math
import time
#import numpy as np
import collections
from collections import deque
import queue
import copy


#X = str(input()).split()
#a = [int(x) for x in input().split()]


HW = str(input()).split()
H = int(HW[0])
W = int(HW[1])
N = int(input())

Gr = [[0]*W for i in range(H)]

A = [int(x) for x in input().split()]

countH = 0
countW = 0

for i in range(N):
  for j in range(A[i]):
    Gr[countH][countW] = i+1
    countW += 1
    if(countW==W):
      countH += 1
      countW = 0

#print(Gr)

for i in range(H):
  if(i%2 == 0):
    L=[str(a) for a in Gr[i]]
    L=' '.join(L)
    print(L)
  else:
    L=[str(a) for a in reversed(Gr[i])]
    L=' '.join(L)
    print(L)


