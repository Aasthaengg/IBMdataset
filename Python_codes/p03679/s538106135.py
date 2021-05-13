x, a, b = map(int, input().split())
expire_limit = x + a
if b > expire_limit:
  print('dangerous')
elif b > a and a - b < expire_limit:
  print('safe')
else:
  print('delicious')