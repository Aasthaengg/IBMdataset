N, M = map(int, input().split())
A = [0 for i in range(N+1)]
for i in range(M):
  a, b = map(int, input().split())
  A[a] += 1
  A[b] += 1
for i in range(1, N+1):
  print(A[i])