x,y = input().split()

a = ord(x)
b = ord(y)
if a<b:
  print("<")
elif a>b:
  print(">")
else:
  print("=")