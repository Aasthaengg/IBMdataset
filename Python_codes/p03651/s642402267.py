import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)

if K > A[-1]:
    print('IMPOSSIBLE')
    exit()

keep = A[0]
for i in range(1, N):
    keep = math.gcd(keep, A[i])
if K % keep == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
