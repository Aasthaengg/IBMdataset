x, a, b = map(int, input().split())


if x + a - b < 0:
  print('dangerous')
elif a - b >= 0:
  print("delicious")
else:
  print("safe")