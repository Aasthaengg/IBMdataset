# -*- coding: utf-8 -*-
 
## Library
 
import sys
from fractions import gcd
import math
from math import ceil,floor
import collections
from collections import Counter
import itertools
 
## input
 
# N=int(input())
# A,B,C,D=map(int, input().split())
# S = input()
# yoko = list(map(int, input().split()))
# tate = [int(input()) for _ in range(N)]
# N, M = map(int,input().split()) 
#    P = [list(map(int,input().split())) for i in range(M)]
 
N=int(input())
H= list(map(int, input().split()))

count = 0
tmp = 0

for i in range(1,N):
    if H[i-1] >= H[i]:
        tmp += 1
    else:
        count = max(count,tmp)
        tmp = 0
    if i == N-1:
        count = max(count,tmp)       

print(count)