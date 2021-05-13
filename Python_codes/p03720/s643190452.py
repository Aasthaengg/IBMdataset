N, M = list(map(int, input().split()))
A = [0 for _ in range(N)]

for i in range(M):
   a, b = list(map(int, input().split()))
   A[a-1] += 1
   A[b-1] += 1

for i in range(N):
  print(A[i])

