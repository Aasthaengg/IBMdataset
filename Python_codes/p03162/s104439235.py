n = int(input())
A, B, C = [], [], []

for i in range(n):
  a, b, c = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)

dp_a, dp_b, dp_c = [0] * n, [0] * n, [0] * n
dp_a[0] = A[0]
dp_b[0] = B[0]
dp_c[0] = C[0]

for i in range(1, n):
  dp_a[i] = max(dp_b[i-1], dp_c[i-1]) + A[i]
  dp_b[i] = max(dp_c[i-1], dp_a[i-1]) + B[i]
  dp_c[i] = max(dp_a[i-1], dp_b[i-1]) + C[i]
print(max(dp_a[-1], dp_b[-1], dp_c[-1]))