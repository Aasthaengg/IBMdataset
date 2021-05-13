N, M = list(map(int, input().split()))
ab = []
c = []
for i in range(M):
  ab.append(list(map(int, input().split())))
  c.append(list(map(int, input().split())))

A = [10 ** 10] * (1 << N)
C = []
for i in range(M):
  t = 0
  cc = c[i]
  a, b = ab[i]
  for j in cc:
    t |= 1 << (j - 1)
  C.append([t, a])
  A[t] = min(A[t], a)

for i in range(1, N + 1):
  n = (1 << i) - 1
  while n < (1 << N):
    for j in range(M):
      k, a = n | C[j][0], C[j][1]
      A[k] = min(A[k], A[n] + a)
    x = n & -n
    y = n + x
    n = ((n & ~y) // x >> 1) | y

if A[-1] == 10 ** 10:
  print(-1)
else:
  print(A[-1])

