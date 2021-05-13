x,y = map(format, input().split())

if x == y:
  print('=')
elif x<y:
  print('<')
else:
  print('>')