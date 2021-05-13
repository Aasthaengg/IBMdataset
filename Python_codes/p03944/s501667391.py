w, h, n = map(int, input().split())
origin = [0,0]
edge = [w,h]
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
      if origin[0] < x:
          origin[0] = x
    elif a == 2:
      if x < edge[0]:
          edge[0] = x
    elif a == 3:
      if origin[1] < y:
          origin[1] = y
    else:
      if y < edge[1]:
          edge[1] = y

width = edge[0] - origin[0]
height = edge[1] - origin[1]
if width < 0:
  width = 0
if height < 0:
  height = 0

print(width * height)