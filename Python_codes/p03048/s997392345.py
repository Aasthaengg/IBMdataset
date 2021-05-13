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

R,G,B,N = map(int,input().split()) 

ans = 0
tmp1 = N//R + 1

for i in range(tmp1):
    tmp2 = (N - R*i)//G + 1
    for j in range(tmp2):
        if (N - R*i - G*j)%B == 0:
            ans += 1



print(ans)