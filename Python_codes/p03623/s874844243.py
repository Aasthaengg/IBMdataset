x,a,b = input().split()
x = int(x)
a = int(a)
b = int(b)
if (x-a)*(x-a) <= (x-b)*(x-b) :
  print("A")
else :
  print("B")