x,a,b = input().split()
x = int(x)
a = int(a)
b = int(b)
if abs(x-a) <= abs(x-b) :
  print("A")
else :
  print("B")