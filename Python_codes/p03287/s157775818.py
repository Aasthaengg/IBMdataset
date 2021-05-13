N, M = map(int, input().split())
A = list(map(int, input().split()))
D = {0:1}
for i in A:
  i %= M
S = 0
for i in range(N):
  S += A[i]
  S %= M
  if S % M in D:
    D[S%M] += 1
  else:
    D[S%M] = 1
perm = 0
for i in D:
  perm += (D[i] * (D[i] - 1)) // 2
print(perm)