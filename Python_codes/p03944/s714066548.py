w,h,n=map(int, input().split())
x=[]
y=[]
a=[]
for i in range(n):
  s=input().split()
  x.append(int(s[0]))
  y.append(int(s[1]))
  a.append(int(s[2]))
x_l=0
x_h=w
y_l=0
y_h=h
for i in range(n):
  if a[i]==1:
    if x_l<x[i]:
      x_l=x[i]
  elif a[i]==2:
    if x_h>x[i]:
      x_h=x[i]
  elif a[i]==3:
    if y_l<y[i]:
      y_l=y[i]
  else:
    if y_h>y[i]:
      y_h=y[i]
if x_h>x_l and y_h>y_l:
  print((x_h-x_l)*(y_h-y_l))
else:
  print("0")
