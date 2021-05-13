from numba import jit

@jit
def solve(N, K, A):
  for k in range(K):
    B = [0] * N
    for i in range(N):
      l = max(0, i - A[i])
      r = i + A[i] + 1
      B[l] += 1
      if r < N:
        B[r] -= 1

    for j in range(N - 1):
      B[j + 1] += B[j]
  
    if A == B:
      return B
    A = B
  return B
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = solve(N, K, A)
for b in B:
  print(b, end=" ")
