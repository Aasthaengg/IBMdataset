N, M = map(int, input().split())
L = [0] * N
D = {}
c = 1
for i in range(M):
  A, B = map(int, input().split())
  if L[A - 1] == L[B - 1] == 0:
    D[c] = set()
    D[c].add(A)
    D[c].add(B)
    L[A - 1] = c
    L[B - 1] = c
    c += 1
  elif L[A - 1] == 0:
    D[L[B - 1]].add(A)
    L[A - 1] = L[B - 1]
  elif L[B - 1] == 0:
    D[L[A - 1]].add(B)
    L[B - 1] = L[A - 1]
  elif L[A - 1] != L[B - 1]:
    if len(D[L[A - 1]]) < len(D[L[B - 1]]):
      A, B = B, A
    D[L[A - 1]] |= D[L[B - 1]]
    for j in D.pop(L[B - 1]):
      L[j - 1] = L[A - 1]
  #print(L, D, sep = "\n")
print(len(D) + L.count(0) - 1)