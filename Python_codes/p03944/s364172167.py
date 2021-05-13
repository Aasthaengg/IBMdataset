W, H, N = map(int, input().split())
p = 0
q = W
r = 0
s = H
for i in range(N):
  x, y, a = map(int, input().split())
  if a == 1:
    p = max(p, x)
  elif a == 2:
    q = min(q, x)
  elif a == 3:
    r = max(r, y)
  else:
    s = min(s, y)
print(max(q - p, 0) * max(s - r, 0))