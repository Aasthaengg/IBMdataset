a,b,c,d=map(int,input().split())
L = a+b
R = c+d
if L<R:
  print("Right")
elif R<L:
  print("Left")
else:
  print("Balanced")