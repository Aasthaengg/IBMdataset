w,h,n = map(int, input().split())

o,p,q,r = 0,0,0,0
for _ in range(n):
  x,y,a = map(int, input().split())
  if a == 1:
    o = max(o, x)
  elif a == 2:
    p = max(p, w-x)
  elif a == 3:
    q = max(q, y)
  elif a == 4:
    r = max(r, h-y)

w -= o+p
h -= q+r
if w <= 0 or h <= 0:
  print(0)
else:
  print(w*h)