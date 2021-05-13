x,y=list(input().split())
x=int(x,16)
y=int(y,16)
if x>y:
  print('>')
elif x==y:
  print('=')
else:
  print('<')