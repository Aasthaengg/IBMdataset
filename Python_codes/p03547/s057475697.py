X,Y = input().split()

x = "ABCDEF".index(X)
y = "ABCDEF".index(Y)

if x==y:
  print("=")
elif x>y:
  print(">")
else:
  print("<")