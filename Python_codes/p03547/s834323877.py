a, b= map(str, input().split())
if a == b:
  print('=')
else:
  a = int(a, 16)
  b = int(b, 16)
  if a > b:
    print('>')
  else:
    print('<')