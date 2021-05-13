N, T = map(int, input().split())
A = list(map(int, input().split()))
S = 0
for i in range(N-1):
  if A[i+1] - A[i] > T:
    S += T
  else:
    S += A[i+1] - A[i]
S += T
print(S)