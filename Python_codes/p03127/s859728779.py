import sys
import math


N = int(input())
A = list(map(int, input().split()))



g = A.pop(0)
for c in A:
    g = math.gcd(g,c)

print(g)