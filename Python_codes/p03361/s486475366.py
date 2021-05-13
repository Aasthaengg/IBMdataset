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
 
H,W=map(int, input().split())
S = []

S.append(['.']*(W+2))
for _ in range(H):
    S.append(['.']+list(input())+['.'])
S.append(['.']*(W+2))

for i in range(1,H+1):
    for j in range(1,W+1):
        #print(i,j,S[i][j])
        if S[i][j] == "#" and S[i-1][j] == "." and S[i+1][j] == "." and  S[i][j-1] == "." and  S[i][j+1]== ".":
            print("No")
            sys.exit()

print("Yes")