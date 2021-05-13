x,a,b=input().split()
x=int(x)
a=int(a)
b=int(b)
if x<a:
	distance_xa=a-x
else:
    distance_xa=x-a
if x<b:
  distance_xb=b-x
else:
  distance_xb=x-b
if distance_xa<distance_xb:
  print("A")
else:
  print("B")