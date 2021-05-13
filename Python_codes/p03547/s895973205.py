c,d=map(str,input().split())
n=sorted([c,d])
a=n.index(c)
b=n.index(d)
if a>b:
  print('>')
elif a==b:
  print('=')
else:
  print('<')