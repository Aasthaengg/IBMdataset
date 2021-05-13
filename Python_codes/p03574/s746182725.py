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

# n=int(input())
# A,B,C,D=map(int, input().split())
# string = input()
# yoko = list(map(int, input().split()))
# tate = [int(input()) for _ in range(N)]
# N, M = map(int,input().split()) 
#    P = [list(map(int,input().split())) for i in range(M)]
#    S = []
#    for _ in range(N):
#        S.append(list(input()))

H,W= map(int,input().split()) 
S = []
S.append(['.']*(W+2))
for _ in range(H):
    S.append(['.']+list(input())+['.'])
S.append(['.']*(W+2))

for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j] == "#":
            print("#", end='')
        else:
            Stmp = S[i-1][j-1]+S[i-1][j]+S[i-1][j+1]+S[i][j-1]+S[i][j+1]+S[i+1][j-1]+S[i+1][j]+S[i+1][j+1]
            print(Stmp.count("#"), end='')
    print()
