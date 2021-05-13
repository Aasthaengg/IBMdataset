import math

N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

for i in range(min(41, K)):
  B = [0] * N
  for n, A_n in enumerate(A):
    B_min = max(0, n-A_n)
    b_max = min(N-1, n+A_n)
    B[B_min] += 1
    if b_max+1 < N:
      B[b_max+1] -= 1
  
  sum = 0
  for n in range(len(A)):
    sum += B[n]
    A[n] = sum

print(" ".join(list(map(str, A))))