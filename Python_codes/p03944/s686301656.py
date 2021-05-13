w, h, n = map(int, input().split())
num_w = 0
num_h = 0

for i in range(n):
  x, y, a = map(int, input().split())
  if a == 1:
    if num_w < x:
      num_w = x
  elif a == 2:
    if w > x:
      w = x
  elif a == 3:
    if num_h < y:
      num_h = y
  else:
    if h > y:
      h = y
      
cnt_w = w-num_w
cnt_h = h-num_h

if cnt_w < 0 or cnt_h < 0:
  print(0)
else:
  print(cnt_w*cnt_h)