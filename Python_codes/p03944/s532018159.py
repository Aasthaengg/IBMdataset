w, h , n = map(int , input().split())

left = 0
right = w
lower = 0
upper = h

for i in range(n):
  x, y, a = map(int, input().split())
  
  if a == 1:
    left = max(left, x)
  elif a == 2:
    right = min(x, right)
  elif a == 3:
    lower = max(lower, y)
  elif a == 4:
    upper = min(y, upper)

if left > right or lower > upper:
    print(0)
else:
    print((right-left)*(upper-lower))