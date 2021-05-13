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

N,K = map(int,input().split()) 

ans = float(0)

if K <= N:
    ans += (N-K+1)/N
    X = K
else:
    X = N+1

for i in range(1,X):
    tmp = float(1/N)
    tmp2 = i
    while tmp2 < K:
        tmp2 *= 2
        tmp /= 2
    ans += tmp

print(ans)