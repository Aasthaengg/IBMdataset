W, H, N = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
L, R, U, D = 0, W, H, 0
for p in P:
  x, y, a = p
  if a == 1:
    L = max(L, x)
  elif a == 2:
    R = min(R, x)
  elif a == 3:
    D = max(D, y)
  else:
    U = min(U, y)
print(max(U-D, 0) * max(R-L, 0))
