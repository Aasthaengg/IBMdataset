N, K = map(int, input().split())
A = list(map(int, input().split()))
D = [0 for i in range(N)]
for i in range(1, N):
  D[i] = D[i-1] + abs(A[i-1] - A[i])
  for j in range(2, K + 1):
    if i - j < 0:
      break
    D[i] = min(D[i], D[i-j] + abs(A[i-j] - A[i]))
print(D[-1])