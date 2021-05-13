[w, h, n] = list(map(int, input().split()))
list_x1 = []
list_x2 = []
list_y3 = []
list_y4 = []
for i in range(n):
  xya = list(map(int, input().split()))
  if xya[2] == 1:
    list_x1.append(xya[0])
  if xya[2] == 2:
    list_x2.append(xya[0])
  if xya[2] == 3:
    list_y3.append(xya[1])
  if xya[2] == 4:
    list_y4.append(xya[1])
try:
  min_x = min(list_x2)
except ValueError:
  pass  
try:
  max_x = max(list_x1)
except ValueError:
  pass  
try:
  min_y = min(list_y4)
except ValueError:
  pass  
try:
  max_y = max(list_y3)
except ValueError:
  pass  
try:
  w =min_x
except NameError:
  pass
try:
  w -= max_x
except NameError:
  pass
try:  
  h = min_y
except NameError:
  pass
try:
  h -= max_y
except NameError:
  pass
if w > 0 and h > 0:
  print(w*h)
else:
  print(0)