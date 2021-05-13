x,y=map(str,input().split())
xx=ord(x)
yy=ord(y)
if xx<yy:
  print("<")
elif xx==yy:
  print("=")
else:
  print(">")