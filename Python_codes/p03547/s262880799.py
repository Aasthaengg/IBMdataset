x, y = list(map(str, input().split()))
if x == 'A':
  x = 10
elif x == 'B':
  x = 11
elif x == 'C':
  x = 12
elif x == 'D':
  x = 13
elif x == 'E':
  x = 14
elif x == 'F':
  x = 15
if y == 'A':
  y = 10
elif y == 'B':
  y = 11
elif y == 'C':
  y = 12
elif y == 'D':
  y = 13
elif y == 'E':
  y = 14
elif y == 'F':
  y = 15
if x > y:
  print('>')
elif x == y:
  print('=')
else:
  print('<')