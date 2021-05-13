import itertools
import math
import fractions
import functools
import copy
n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

sum = 0
for i in range(n):
    if v[i] > c[i]:
        sum += v[i] - c[i]
print(sum)