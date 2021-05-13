from sys import stdin
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

k = int(stdin.readline().rstrip())

d = 0
for i in range(1,k+1):
    for j in range(i+1,k+1):
        for l in range(j+1,k+1):
            d = d + 6*reduce(gcd, [i,j,l])

for i in range(1,k+1):
    for j in range(1,k+1):
        if j != i: d = d + 3*reduce(gcd, [i,j])

for i in range(1,k+1):
    d = d + i

print (d)