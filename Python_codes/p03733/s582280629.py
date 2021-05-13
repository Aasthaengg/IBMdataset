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
 
N,T=map(int, input().split())
time = list(map(int, input().split()))

ans = T

for i in range(1,N):
    if time[i]-time[i-1] >= T:
        ans += T
    else:
        ans += T
        ans = ans - (T-(time[i]-time[i-1]))

print(ans)