class Tree():
  def __init__(s, n):
    s.L = [-1] * n
  def root(s, x):
    if s.L[x] < 0:
      return x, -s.L[x]
    a, b = s.root(s.L[x])
    s.L[x] = a
    return a, b
  def merge(s, a, b):
    ra, sa = s.root(a)
    rb, sb = s.root(b)
    if ra != rb:
      if sa < sb:
        s.L[ra] = rb
        s.L[rb] -= sa
      else:
        s.L[rb] = ra
        s.L[ra] -= sb
      return True
    return False


N, K, L = list(map(int, input().split()))
pq = [list(map(int, input().split())) for _ in range(K)]
rs = [list(map(int, input().split())) for _ in range(L)]

R = Tree(N)
T = Tree(N)

for a, b in pq:
  a -= 1
  b -= 1
  R.merge(a, b)

for a, b in rs:
  a -= 1
  b -= 1
  T.merge(a, b)

RL = [0] * N
for i in range(N):
  RL[i] = R.root(i)[0]

TL = [0] * N
for i in range(N):
  TL[i] = T.root(i)[0]

D = {}
for i in range(N):
  if RL[i] not in D:
    D[RL[i]] = {}
    D[RL[i]][TL[i]] = 1
  else:
    if TL[i] not in D[RL[i]]:
      D[RL[i]][TL[i]] = 1
    else:
      D[RL[i]][TL[i]] += 1

for i in range(N):
  print(D[RL[i]][TL[i]], end = " ")
