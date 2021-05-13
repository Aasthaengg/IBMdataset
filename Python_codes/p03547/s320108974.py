X, Y = input().split()
x = ord(X); y = ord(Y)

if x < y:
  print('<')
elif x == y:
  print('=')
else:
  print('>')