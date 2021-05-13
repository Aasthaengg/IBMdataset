X,Y = map(str, input().split())
l = ['A','B','C','D','E','F']
if l.index(X)>l.index(Y):
  print('>')
elif l.index(X)<l.index(Y):
  print('<')
else:
  print('=')