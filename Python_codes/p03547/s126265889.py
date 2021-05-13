x,y=input().split()
L=[x,y]
L.sort()
if x==y:
  print('=')
elif L[0]==x:
  print('<')
else:
  print('>')
