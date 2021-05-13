w,h,x,y=[int(x) for x in input().split()]
a=w*h/2
if x==w/2 and y==h/2:
  b=1
else:
  b=0
print(a,b)