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
 
N = int(input())
H = list(map(int, input().split()))

ans = 0
while sum(H) > 0:
    tmp = 0
    for i in range(N):
        if H[i] > 0:
            H[i] -= 1
            tmp += 1
        elif H[i] == 0 and tmp > 0:
            ans += 1
            tmp = 0
        if i == N-1 and tmp > 0:
            ans += 1

print(ans)