N = int(input())
A = list(map(int, input().split()))
import numpy as np
B = []
m = N//2
b = 0
for i in range(m):
  b = b + A[2*i] - A[2*i+1]
b += A[N-1]
B.append(b)
n = 0
for i in range(N-1):
  c = 2*A[i]-B[n]
  B.append(c)
  n += 1
B=[str(d) for d in B]
B=" ".join(B)
print(B)