s = list(input())
a = 0
b = 0
c = 0
for v in s:
  if v == 'a':
    a += 1
  elif v == 'b':
    b += 1
  else:
    c += 1
if abs(a-b) < 2 and abs(b-c) < 2 and abs(a-c) < 2:
  print('YES')
else:
  print('NO')