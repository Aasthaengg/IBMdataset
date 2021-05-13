from functools import reduce
import math

k = int(input())

s = 0

def gcd(*numbers):
    return reduce(math.gcd, numbers)

for i in range(1,k+1):
    for j in range(1,k+1):
        for l in range(1,k+1):
            s += gcd(i,j,l)

print(s)

