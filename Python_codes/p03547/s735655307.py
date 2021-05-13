x,y = input().split()
l = ["A","B","C","D","E","F"]
if l.index(x) < l.index(y):
  print("<")
elif l.index(x) > l.index(y):
  print(">")
else:
  print("=")