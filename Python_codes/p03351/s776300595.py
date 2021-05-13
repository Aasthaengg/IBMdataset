a,b,c,d=input().split()
if abs(int(a)-int(c))<=int(d) or (abs(int(a)-int(b))<=int(d) and abs(int(b)-int(c))<=int(d)):
  print("Yes")
else:
  print("No")