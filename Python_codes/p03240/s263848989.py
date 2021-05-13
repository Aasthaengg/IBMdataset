N = int(input())
X, Y, H = [0]*N, [0]*N, [0]*N
for i in range(N):
  X[i], Y[i], H[i] = map(int, input().split())
  
for Cx in range(0, 100+1):
  for Cy in range(0, 100+1):
    H_TOP = 1
    for i in range(N):
      if H[i]:
        H_TOP = H[i] + abs(X[i] - Cx) + abs(Y[i] - Cy)
    ok = True
    for i in range(N):
      if (max(H_TOP - abs(X[i] - Cx) - abs(Y[i] - Cy), 0) != H[i]):
        ok = False
    if ok:
      print(Cx, Cy, H_TOP)