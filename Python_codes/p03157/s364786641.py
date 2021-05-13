H, W = map(int, input().split())
S = []
for i in range(H):
  ss = input()
  S.append(ss)
UF = list(range(H*W))
def par(m):
  if UF[m] == m:
    return m
  r = par(UF[m])
  UF[m] = r
  return r
def unite(m, n):
  i = par(m)
  j = par(n)
  UF[i] = j
for i in range(H):
  for j in range(W):
    if i+1 < H and S[i][j] != S[i+1][j]:
      unite(i*W+j, (i+1)*W+j)
    if j+1 < W and S[i][j] != S[i][j+1]:
      unite(i*W+j, i*W+j+1)
nsb = [0]*(H*W)
nsw = [0]*(H*W)
for i in range(H):
  for j in range(W):
    p = par(i*W+j)
    if S[i][j] == "#":
      nsb[p] += 1
    if S[i][j] == ".":
      nsw[p] += 1
r = 0
for p in range(H*W):
  r += nsb[p]*nsw[p]
print(r)
#  print(UF[i*W:(i+1)*W])
