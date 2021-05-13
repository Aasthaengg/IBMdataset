# -*- coding: utf-8 -*-
 
## Library
 
import sys
from fractions import gcd
import math
from math import ceil,floor
import collections
from collections import Counter
import itertools
import copy

## input
 
# N=int(input())
# A,B,C,D=map(int, input().split())
# S = input()
# yoko = list(map(int, input().split()))
# tate = [int(input()) for _ in range(N)]
# N, M = map(int,input().split()) 
#    P = [list(map(int,input().split())) for i in range(M)]
#    S = []
#    for _ in range(N):
#        S.append(list(input()))

N=int(input())
T,A=map(int, input().split())
H = list(map(int, input().split()))

ans = 0
tmp = abs(A - (T - H[0]*0.006))

for i in range(1,N):
    tmp2 = abs(A - (T - H[i]*0.006))
    if tmp2 < tmp:
        ans = i
        tmp = tmp2


print(ans+1)