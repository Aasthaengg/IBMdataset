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
#    P = [list(map(int,input().split())) for i in range(M)]
 
N=int(input())
S = [int(input()) for _ in range(N)]

tmp = sum(S)

if tmp%10 != 0:
    print(tmp)
else:
    S.sort()
    for i in range(N):
        if S[i]%10 != 0:
            print(tmp-S[i])
            sys.exit()
    print(0)