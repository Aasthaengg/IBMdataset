s='ABCDEF'
a,b=input().split()
x=s.find(a)
y=s.find(b)
if x==y:
  print('=')
elif x>y:
  print('>')
else:
  print('<')