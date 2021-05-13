x, y=map(int, input().split())
if x==1:
  a=300000
elif x==2:
  a=200000
elif x==3:
  a=100000
else:
  a=0
  
if y==1:
  b=300000
elif y==2:
  b=200000
elif y==3:
  b=100000
else:
  b=0
  
if x==1 and y==1:
  c=400000
else:
  c=0
  
print(a+b+c)