# -*- coding: utf-8 -*-

## Library

import sys
from fractions import gcd
import math
from math import ceil,floor
import collections

## input

# n=int(input())
# A,B,C,D=map(int, input().split())
# string = input()
# yoko = list(map(int, input().split()))
# tate = [int(input()) for _ in range(N)]
# N, M = map(int,input().split()) 
#    P = [list(map(int,input().split())) for i in range(M)]

N = int(input())
A = list(map(int, input().split()))

## Logic

ans = [0,0,0,0,0,0,0,0]
tmp = 0

for i in range(0,N):
    if A[i] >= 3200:
        tmp += 1
    else:
        ans[A[i]//400] = 1

print(max(1,sum(ans)),sum(ans)+tmp)

