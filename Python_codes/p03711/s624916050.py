x, y = map(int, input().split())
X, Y = 0, 0
l = [4, 6, 9, 11]
if x == 2:
  X = 3
elif x in l:
  X = 2
else:
  X = 1
if y == 2:
  Y = 3
elif y in l:
  Y = 2
else:
  Y = 1
if X == Y:
  print("Yes")
else:
  print("No")