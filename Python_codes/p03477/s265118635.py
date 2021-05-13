#!/usr/bin/python3

import sys
# input = sys.stdin.readline
sys.setrecursionlimit(100000)
INF = float('inf')
MOD = 10**9+7
EPS = 10**-7

#N = int(input())
#A = [int(x) for x in input().split()]
#V = [[0] * 100 for _ in range(100)]

A,B,C,D = [int(x) for x in input().split()]

if A+B == C+D:
    ans = 'Balanced'
elif A+B > C+D:
    ans = 'Left'
else: 
    ans = 'Right'

print(ans)