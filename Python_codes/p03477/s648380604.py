A,B,C,D=map(int,input().split())
a=A+B
b=C+D
if a>b:
  print("Left")
elif a==b:
  print("Balanced")
else:
  print("Right")