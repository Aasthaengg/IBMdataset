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

N,M=map(int, input().split())
AB=[list(map(int,input().split())) for i in range(N)]
CD=[list(map(int,input().split())) for i in range(M)]

tmp = 10**10
for i in range(N):
    kyori = tmp
    ans = 0
    for j in range(M):
        tmp2 = abs(AB[i][0]-CD[j][0])+abs(AB[i][1]-CD[j][1])
        if kyori > tmp2:
            kyori = tmp2
            ans = j+1
    print(ans)
