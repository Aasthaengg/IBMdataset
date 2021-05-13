s = 'ABCDEF'
a,b = map(str, input().split())
if s.index(a) < s.index(b):
  print('<')
elif s.index(a) > s.index(b):
  print('>')
else:
  print('=')