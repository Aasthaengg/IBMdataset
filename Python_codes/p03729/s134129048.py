a=input()

b=a.split(' ')

if b[0][-1]==b[1][0] and b[1][-1]==b[2][0]:
  print('YES')
else:
  print('NO')