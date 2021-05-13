a1, a2 = map(str, input().split())
x = 'ABCDEF'
c = x.index(a1)
d = x.index(a2)
if c == d:
  print('=')
elif c > d:
  print('>')
else:
  print('<')