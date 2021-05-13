N, M = map(int, input().split())
a = []
b = []
c = []
d = []
ans = []

for n in range(N):
  A, B = map(int, input().split())
  a.append(A)
  b.append(B)

for m in range(M):
  C, D = map(int, input().split())
  c.append(C)
  d.append(D)

for i in range(N):
  l = []
  for j in range(M):
    l.append(abs(a[i] - c[j]) + abs(b[i] - d[j]))
  print(l.index(min(l))+1)