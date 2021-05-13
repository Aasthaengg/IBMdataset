def possible(b):
    print('POSSIBLE' if b else 'IMPOSSIBLE')
    exit()

n, k = map(int, input().split())
A = list(set(map(int, input().split())))
n = len(A)

if k in A:
    possible(True)

if k > max(A):
    possible(False)

if n == 1:
    possible(False)

A.sort()
D = [A[i + 1] - A[i] for i in range(n - 1)]
from fractions import *
g = D[0]
for d in D:
    g = gcd(g, d)

possible(k % g == 0)