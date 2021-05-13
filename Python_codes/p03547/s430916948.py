x,y = input().split()
z = ord(x)
w = ord(y)
if z < w:
  print("<")
elif z > w:
  print(">")
else:
  print("=")