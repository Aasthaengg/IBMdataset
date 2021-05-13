def down(H, n):
  x = min(H)
  n += x
  for i in range(len(H)):
    H[i] -= x
  return H, n

N = int(input())
H = list(map(int, input().split()))
n = 0
H, n = down(H, n)

while not all(h == 0 for h in H):
  L = []
  H0 =[]
  for h in H:
    if h != 0:
      L.append(h)
    else:
      if L:
        L, n = down(L, n)
      H0 += L
      H0.append(0)
      L = []
  if L:
    L, n = down(L, n)
    H0 += L
  H = H0

print(n)