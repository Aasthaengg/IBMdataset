A,B,C,D=map(int,input().split())
w=A+B-C-D
if w==0:
  print("Balanced")
elif w>0:
  print("Left")
else:
  print("Right")