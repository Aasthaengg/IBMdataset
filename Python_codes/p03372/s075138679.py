N, C = map(int, input().split())
X = []
V = []
for _ in range(N):
  x, v = map(int, input().split())
  X.append(x)
  V.append(v)

A = [0] * (N + 1)
A_max = [0] * (N + 1)
B = [0] * (N + 1)
B_max = [0] * (N + 1)
a_sum = 0
b_sum = 0
for i in range(N):
  a_sum += V[i]
  A[i + 1] = a_sum - X[i]
  A_max[i + 1] = max(A_max[i], A[i + 1])
  b_sum += V[- i - 1]
  B[i + 1] = b_sum - (C - X[- i - 1])
  B_max[i + 1] = max(B_max[i], B[i + 1])

X = [0] + X
V = [0] + V

m = max(0, A_max[-1], B_max[-1])
for i in range(1, N + 1):
  m = max(m, A[i] + B_max[N - i] - X[i], B[i] + A_max[N - i] - (C - X[N - i + 1]))

print(m)