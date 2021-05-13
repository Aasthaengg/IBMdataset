N,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.sort()
if A[-1] < K:
    print("IMPOSSIBLE")
    exit()
if K in A:
    print("POSSIBLE")
    exit()
from fractions import gcd
n = A[0]
for i in range(1,N):
    n = gcd(A[i],n)
if K % n == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")