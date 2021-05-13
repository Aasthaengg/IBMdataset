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


S = input()

ans = 0
tmp = 0
for i in range(len(S)):
    if S[i] == "W":
        ans += i-tmp
        tmp += 1

print(ans)