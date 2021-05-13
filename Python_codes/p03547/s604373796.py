alf=['A','B','C','D','E','F']
x,y=input().split()
if alf.index(x)<alf.index(y):
  print('<')
elif alf.index(x)>alf.index(y):
  print('>')
else:
  print('=')