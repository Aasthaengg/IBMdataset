#!/usr/bin/env python
import math

chebyshev = []

n = int(input())

x = input().split()
y = input().split()

for i in range(n):
    x[i] = int(x[i])
for i in range(n):
    y[i] = int(y[i])

for p in range(3):
    total = 0
    for i in range(n):
        total += (math.fabs(x[i]-y[i]))**(p+1)
    distance = total**(1/(p+1))
    print("%.5f" % distance)

for i in range(n):
    chebyshev.append(math.fabs(x[i]-y[i]))
print("%.5f" % max(chebyshev))