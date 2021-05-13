x, a, b = (int(i) for i in input().split())

n = b - a
if n <= 0:
  print('delicious')
elif n <= x:
  print('safe')
else:
  print('dangerous')