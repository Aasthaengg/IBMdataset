N = int(input())
A = list(map(int, input().split()))
X = [0] * N
for i in range(N):
  X[0] += (-1) ** i * A[i]
print(X[0], end = " ")
for i in range(N - 1):
  X[i + 1] = X[i] * (-1) + 2 * A[i]
  print(X[i + 1], end = " ")
