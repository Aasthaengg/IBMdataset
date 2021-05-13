a,b,c,d=[int(s) for s in input().split()]
x=a+b-c-d
if x>0:
  print("Left")
elif x==0:
  print("Balanced")
else:
  print("Right")