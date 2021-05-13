a,b=map(int,input().split())
total=a*(a+2*b-1)//2
x=b
y=a+b-1
if abs(x)<abs(y):
  z=x
else:
  z=y
if x<=0 and y>=0:
  print(total)
else:
  print(total-z)
