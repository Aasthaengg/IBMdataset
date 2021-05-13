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

# n=int(input())
# A,B,C,D=map(int, input().split())
# string = input()
# yoko = list(map(int, input().split()))
# tate = [int(input()) for _ in range(N)]
# N, M = map(int,input().split()) 
#    P = [list(map(int,input().split())) for i in range(M)]

N = int(input())
A = [int(input()) for _ in range(N)]
C = collections.Counter(A)
data = list(C.values())

ans = 0

for i in range(len(data)):
    if data[i] % 2 == 1:
        ans+=1

print(ans)