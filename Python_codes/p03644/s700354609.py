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

N=int(input())


while N>0:
    tmp = N
    while tmp%2 == 0:
        tmp = tmp//2
    if tmp == 1:
        print(N)
        sys.exit()
    N -= 1