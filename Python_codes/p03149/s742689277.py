s = set(input().split())
a = {'1','9','7','4'}
s = s&a
if len(s) == 4:
  print('YES')
else:
  print('NO')