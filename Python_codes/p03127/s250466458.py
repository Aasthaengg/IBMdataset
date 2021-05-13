N = int(input())
A = list(map(int, input().split()))

import math

g = math.gcd(A[0], A[0])
for a in A:
    g = math.gcd(g, a)
print(g)
