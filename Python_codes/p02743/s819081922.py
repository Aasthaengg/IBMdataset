a,b,c=input().split(' ')
a=int(a)
b=int(b)
c=int(c)
if (c-a-b>0) and ((c-a-b)**2>4*a*b):
  print("Yes")
else:
  print("No")