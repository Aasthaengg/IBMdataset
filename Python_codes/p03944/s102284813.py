w,h,n = map(int, input().split())

x1,x2,y1,y2 = 0,0,0,0
for _ in range(n):
  x,y,a = map(int, input().split())
  if a == 1: x1 = max(x1, x)
  if a == 2: x2 = max(x2, w-x)
  if a == 3: y1 = max(y1, y)
  if a == 4: y2 = max(y2, h-y)

w -= x1+x2
h -= y1+y2
if w > 0 and h > 0: print(w*h)
else: print(0)