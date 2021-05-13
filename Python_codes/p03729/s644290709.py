#16:05
a,b,c = input().split()
x = int(a[-1]==b[0]) * int(b[-1]==c[0])
if x == 1:
  print('YES')
else:
  print('NO')