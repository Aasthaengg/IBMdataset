x,y=input().split()
if ord(x) < ord(y):
  print("<")
elif x==y:
  print("=")
else:
  print(">")