x = input()
y = input()
t = ''
for i in range(3):
  t = x[i] + t
if t == y:
  print('YES')
else:
  print('NO')