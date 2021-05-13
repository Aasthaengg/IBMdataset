from math import gcd
N,K = map(int,input().split())
A = list(map(int,input().split()))
val = A[0]
for i in range(1,N):
    val = gcd(val,A[i])
if K % val == 0 and K <= max(A):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
