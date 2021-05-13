N = int(input())
A = list(map(int, input().split()))
A.sort()
from math import gcd
for i in range(N-1):
    a = A[i]
    b = A[i+1]
    a, b = 0, gcd(a,b)
    A[i] = a
    A[i+1] = b
print(A[N-1])