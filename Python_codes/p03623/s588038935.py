x,a,b = [int(i) for i in input().split()]

ax = abs(x-a)
bx = abs(x-b)

if min([ax,bx])==ax:
  print("A")
else:
  print("B")