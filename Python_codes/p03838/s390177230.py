x,y = map(int,input().split())
count = 1

if x*y > 0:
  if x < y:
    count = y - x
  elif x > y:
    count = 2 + abs(y-x)
  elif abs(x) == abs(y):
    count = 0
elif x*y < 0:
  if x > y or x < y:
    count = 1 + abs(abs(x) - abs(y))
  elif abs(x) == abs(y):
    count = 0
else:
  if x != 0:
    count = abs(x)
    if x > 0:
      count += 1
  elif y != 0:
    count = abs(y)
    if y < 0:
      count += 1
  else:
    count = 0

print(count)
