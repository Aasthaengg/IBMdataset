N, K, L = map(int, input().split())
E = [[] for i in range(N)]
for i in range(K):
  p, q = map(int, input().split())
  E[p-1].append(q-1)
  E[q-1].append(p-1)
F = [[] for i in range(N)]
for i in range(L):
  r, s = map(int, input().split())
  F[r-1].append(s-1)
  F[s-1].append(r-1)
C = list(range(N))
for n in range(N):
  if C[n] != n:
    continue
  q = [n]
  while q:
    c = q.pop()
    ds = E[c]
    for d in ds:
      if C[d] != n:
        C[d] = n
        q.append(d)
D = list(range(N))
for n in range(N):
  if D[n] != n:
    continue
  q = [n]
  while q:
    c = q.pop()
    ds = F[c]
    for d in ds:
      if D[d] != n:
        D[d] = n
        q.append(d)
#print(C)
#print(D)
Nums = {}
for i in range(N):
  c, d = C[i], D[i]
  if (c, d) in Nums:
    Nums[(c, d)] += 1
  else:
    Nums[(c, d)] = 1
rs = []
for i in range(N):
  c, d = C[i], D[i]
  r = Nums[(c, d)]
  rs.append(r)
print(" ".join(map(str, rs)))
