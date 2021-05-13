x, a, b = list(map(int, input().split()))
if a - b >= 0:
  print('delicious')
elif 0 < b - a <= x:
  print('safe')
else:
  print('dangerous')