x, y=input().split()
alp='ABCDEF'
if x==y:
  print('=')
elif alp.index(x)<alp.index(y):
  print('<')
else:
  print('>')