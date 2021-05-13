a,b,c,d = [int(x) for x in input().split()]
l = a+b
r = c+d
if r > l:
  print("Right")
elif l > r:
  print("Left")
else:
  print("Balanced")