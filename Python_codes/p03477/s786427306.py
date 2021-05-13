A,B,C,D = map(int,input().split())
l=A+B
r=C+D

if l>r:
  print("Left")
elif l==r:
  print("Balanced")
elif l<r:
  print("Right")
