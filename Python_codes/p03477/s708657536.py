a,b,c,d=list(map(int,input().split()))
x=a+b
y=c+d
if x>y:
  print("Left")
elif x<y:
  print("Right")
else:
  print("Balanced")
