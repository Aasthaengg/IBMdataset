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
#    P = [list(map(int,input().split())) for _ in range(M)]

N,M,C=map(int, input().split())
B=list(map(int, input().split()))
A=[list(map(int,input().split())) for _ in range(N)]

ans = 0

for i in range(N):
    tmp = 0
    for j in range(M):
        tmp += A[i][j]*B[j]
    if tmp+C>0:
        ans += 1

print(ans)
