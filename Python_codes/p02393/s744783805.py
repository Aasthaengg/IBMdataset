a,b,c = map(int, input().split())
if(a>b):
  x=a
  a=b
  b=x 
else:
  pass

if(b>c):
  y=b
  b=c
  c=y
else:
  pass
if(a>b):
  z=a
  a=b
  b=z
else:
  pass
print(a,b,c)

