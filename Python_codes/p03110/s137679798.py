import itertools
import math
import fractions
import functools
import copy
n = int(input())
x = []
u = []
for i in range(n):
    a, b = input().split()
    x.append(float(a))
    u.append(b)

sum = 0
for i in range(n):
    if u[i] == "JPY":
        sum += x[i]
    else:
        sum += x[i]*380000

print(sum)