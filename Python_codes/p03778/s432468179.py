MM = input().split()
W = int(MM[0])
a = int(MM[1])
b = int(MM[2])
if a+W < b:
  print(b-(a+W))
elif (b+W) < a:
  print(a -(b+W))
else:
  print(0)