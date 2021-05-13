lst=['A','B','C','D','E','F']
x,t=input().split()
if lst.index(x) > lst.index(t):
  print('>')
elif lst.index(x) < lst.index(t):
  print('<')
else:
  print('=')