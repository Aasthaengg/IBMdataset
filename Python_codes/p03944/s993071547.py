W, H, N = map(int, input().split())
u = H
d = 0
r = W
l = 0
for _ in range(N):
  x, y, a = map(int, input().split())
  if a == 1:
    l = max(l, x)
  elif a == 2:
    r = min(r, x)
  elif a == 3:
    d = max(d, y)
  else:
    u = min(u, y)
dx = max(0, r - l)
dy = max(0, u - d)
print(dx * dy)