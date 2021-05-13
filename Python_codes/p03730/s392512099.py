A, B, C = map(int, input().split())

import math
N = (A * B) // math.gcd(A, B)

array_A = [0]*N
array_B = [0]*N

for i in range(A, N+1, A):
    array_A[i-1] = 1

for i in range(C, N+1, B):
    array_B[i-1] = 1

possible = 0
for i in range(N):
    possible += array_A[i]*array_B[i]

print("YES" if possible else "NO")