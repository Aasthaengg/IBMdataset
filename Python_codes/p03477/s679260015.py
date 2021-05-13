r=lambda:map(int,input().split())
a,b,c,d=r()
if a+b==c+d:
  print("Balanced")
elif a+b>c+d:
  print("Left")
else:
  print("Right")