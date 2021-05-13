a,b,x = map(int, input().split(' '))
if a > x or b < x-a:
  print('NO')
else:
  print('YES')