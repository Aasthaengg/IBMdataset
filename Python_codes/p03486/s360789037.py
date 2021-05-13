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
 
S = input()
T = input()

if S == T:
    print("No")
    sys.exit()

Sx = ''.join(sorted(S))
Tx = ''.join(sorted(T, reverse=True))

L = []
L.append(Sx)
L.append(Tx)

L.sort()

if L[0] == Sx:
    print("Yes")
else:
    print("No")