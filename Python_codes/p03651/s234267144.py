# coding: utf-8
from fractions import gcd
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
a = 0
for i in range(N):
    a = gcd(a, A[i])
if K % a == 0 and K <= A[-1]:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")