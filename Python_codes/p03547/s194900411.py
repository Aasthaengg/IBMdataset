x,y=input().split()
X=int(x,16)
Y=int(y,16)
if X<Y:
  print("<")
elif X==Y:
  print("=")
else:
  print(">")