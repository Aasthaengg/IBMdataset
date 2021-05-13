a, b, c = input().split()

x = a[-1]
y = b[0]
z = b[-1]
w = c[0]

if x == y and z == w:
  print('YES')
else:
  print('NO')