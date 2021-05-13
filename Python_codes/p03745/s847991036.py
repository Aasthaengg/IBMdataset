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
A=list(map(int, input().split()))

ans = 1
state = "normal"

for i in range(1,N):
    if state == "normal":
        if A[i-1] == A[i]:
            continue
        elif A[i-1] < A[i]:
            state = "up"
        else:
            state = "down"
    elif state == "up":
        if A[i-1] > A[i]:
            state = "normal"
            ans += 1
    elif state == "down":
        if A[i-1] < A[i]:
            state = "normal"
            ans += 1 


print(ans)