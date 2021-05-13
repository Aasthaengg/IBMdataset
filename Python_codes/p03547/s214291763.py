x,y=input().split()
if x=='A':
  a=10
elif x=='B':
  a=11
elif x=='C':
  a=12
elif x=='D':
  a=13
elif x=='E':
  a=14
elif x=='F':
  a=15
else:
  a=int(x)
if y=='A':
  b=10
elif y=='B':
  b=11
elif y=='C':
  b=12
elif y=='D':
  b=13
elif y=='E':
  b=14
elif y=='F':
  b=15
else:
  b=int(y)
if a>b:
  print('>')
elif a<b:
  print('<')
else:
  print('=')