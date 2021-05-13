p = 10 ** 9 + 7
def f(n):
  F = [1] * (n + 1)
  for i in range(n):
    F[i + 1] = F[i] * (i + 1) % p
  return F
def finv(F):
  n = len(F) - 1
  Finv = list(F)
  Finv[n] = pow(F[n], p - 2, p)
  for i in range(n, 0, -1):
    Finv[i - 1] = Finv[i] * i % p
  return Finv
def P(n, k):
  if n < k:
    return 0
  return F[n] * Finv[n - k] % p
N, K = map(int, input().split())
E = [[] for i in range(N)]
for _ in range(N - 1):
  a, b = map(int, input().split())
  E[a - 1].append(b - 1)
  E[b - 1].append(a - 1)
F = f(K)
Finv = finv(F)
cnt = K
V = [0] * N
Q = [0] * N
pos = 1
for i in range(N):
  q = Q[i]
  V[q] = 1
  children = 0
  parent = 0
  for adj in E[q]:
    if V[adj]:
      parent += 1
    else:
      children += 1
      Q[pos] = adj
      pos += 1
  cnt *= P(K - 1 - parent, children)
  cnt %= p
print(cnt)