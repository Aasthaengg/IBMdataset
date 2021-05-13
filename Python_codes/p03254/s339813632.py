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

N,X=map(int, input().split())
A= list(map(int, input().split()))

A.sort()

ans = 0
for i in range(N):
    if i == N-1:
        if A[i] == X:
            ans += 1
    elif A[i] <= X:
        ans += 1
        X = X - A[i]
    else:
        break

print(ans)