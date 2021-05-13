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

S=input()

if len(S)%2==1:
    S = S[:-1]
    if S[:len(S)//2] == S[len(S)//2:]:
        print(len(S))
        sys.exit()

for i in range(len(S)//2):
    S = S[:-2]
    if S[:len(S)//2] == S[len(S)//2:]:
        print(len(S))
        sys.exit()    

