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
 
K,A,B=map(int, input().split())

if B<=A+2:
    print(K+1)
else:
    if K < A-1:
        print(K+1)
    else:
        K = K - (A-1)
        N = A
        if K%2==0:
            N += K//2 * (B-A)
        else:
            N += K//2 * (B-A) + 1
        print(N)
                

