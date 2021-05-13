x, y = map(int, input().split())
if x == - y:
  print(1)
elif x * y < 0:
  print(abs(abs(x) - abs(y)) + 1)
elif x < y:
  print(y - x)
elif x * y:
  print(abs(abs(x) - abs(y)) + 2)
else:
  print(abs(abs(x) - abs(y)) + 1)

