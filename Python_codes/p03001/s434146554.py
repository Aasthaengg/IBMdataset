W, H ,x, y = map(int, input().split())
if W == H:
  if x == W/2 and y == H/2:
    can = 1
  else:
    can = 0
else:
  if x == W/2 or y == H/2:
    if x == W/2 and y == H/2:
      can = 1
    else:
      can = 0
  else:
    if y == (H/W)*x or y == (-H/W)*x:
      can = 0
    else:
      can = 1
 
print('{:.9f}'.format(W*H/2), can)