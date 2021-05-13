x, y = map(str, input().split())

if int(str(x), 16) < int(str(y), 16):
  print('<')
elif int(str(x), 16) == int(str(y), 16):
  print('=')
else:
  print('>')