N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
  c = list(map(int, input().split()))
  C.append(c[0])
  A.append(c[1:])
ans = sum(C) + 1
for n in range(1 << N):
  p = [0 for j in range(M)]
  q = 0
  for i in range(N):
    t = (n >> i) & 1
    q += t * C[i]
    for j in range(M):
      p[j] += t * A[i][j]
  f = 0
  for j in range(M):
    if p[j] < X:
      f = 1
      break
  if f == 0:
    ans = min(ans, q)
if ans > sum(C):
  print(-1)
else:
  print(ans)