X,Y = map(int,input().split())
a = (4*X-Y)/2
b = (Y-2*X)/2
if a.is_integer() and b.is_integer() and a>=0 and b>=0:
  print("Yes")
else:
  print("No")

