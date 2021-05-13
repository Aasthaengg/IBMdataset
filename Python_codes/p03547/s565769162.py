x,y=input().split()
a="ABCDEF".index(x)
b="ABCDEF".index(y)
if a==b:
  print('=')
elif a>b:
  print('>')
else:
  print('<')