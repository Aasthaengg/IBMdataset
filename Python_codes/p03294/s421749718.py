#!/usr/bin/env python3
#import math
import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

N = int(input())
A = list(map(int, input().split()))

g = A[0]
for i in range(1,N):
    g = lcm(g,A[i])
g -= 1

ans = 0
for a in A:
    ans += g % a
print(ans)
