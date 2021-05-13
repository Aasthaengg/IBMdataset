import itertools
import math
import fractions
import functools
import copy

n, k = map(int, input().split())
h = []
for i in range(n):
    h.append(int(input()))

h.sort()
minimum = 10**10
for i in range(n-k+1):
    minimum = min(minimum,h[i+k-1]-h[i])

print(minimum)