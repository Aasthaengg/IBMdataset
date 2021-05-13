import itertools
import math
import fractions
import functools
import copy

n = int(input())
p = []
for i in range(n):
    p.append(int(input()))

print(sum(p)-max(p)//2)