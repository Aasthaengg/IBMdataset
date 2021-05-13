x, y = map(int, input().split())

if x <= y:
  print(min(y - x, 1 + abs(abs(y) - abs(x))))
elif x * y <= 0:
  print(1 + abs(abs(y) - abs(x)))
else:
  print(2 + abs(y - x))