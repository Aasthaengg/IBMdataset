from fractions import gcd
# from math import gcd

N, K = map(int, input().split())
A = list(map(int, input().split()))

M = max(A)

g = A[0]
for a in A:
    g = gcd(g, a)

if K <= M and K % g == 0:
    print ('POSSIBLE')
else:
    print ('IMPOSSIBLE')