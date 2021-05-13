a, b, x = map(int, input().split())
if x < a:
  print('NO')
elif a+b < x:
  print('NO')
else:
  print('YES')
