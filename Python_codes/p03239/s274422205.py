import itertools
import math
import fractions
import functools
import copy

N, T = map(int, input().split())
c= []
t = []
for i in range(N):
     ci, ti = map(int, input().split())
     c.append(ci)
     t.append(ti)

cost = 10**10
for i in range(N):
    if t[i] <= T:
        cost = min(cost,c[i])
if cost == 10**10:
    print("TLE")
else:print(cost)