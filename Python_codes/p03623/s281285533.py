x,a,b=input().split()
x=int(x)
a=int(a)
b=int(b)
y1=x-a
y2=x-b
y1=abs(y1)
y2=abs(y2)
if y1<y2:
  print("A")
else:
  print("B")