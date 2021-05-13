x,y = map(int,input().split())

if y >=x and x>=0:
  ans = y-x
elif x>=y and y >=0:
  if y == 0:
    ans = abs(x)+1
  else:
    ans = 1+(x-y)+1
elif y>=0 and 0 >=x:
  if abs(y) >= abs(x):
    ans = y+x+1
  else:
    if y == 0:
      ans = y-x
    else:
      ans = -y-x+1
elif x>=0 and 0>=y:
  if abs(x) >= abs(y):
    ans = y+x+1
  else:
    ans = -y-x+1
elif 0>=x and x>=y:
  if x == 0:
    ans = 0-y+1
  else:
    ans = 1-y+x+1
elif 0>=y and y>= x:
  ans = y-x
else:
  print(z)
print(ans)