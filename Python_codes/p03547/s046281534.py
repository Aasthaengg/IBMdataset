l = ["A", "B", "C", "D", "E", "F"]
x, y = map(str, input().split())
if l.index(x) > l.index(y):
  print(">")
elif l.index(x) < l.index(y):
  print("<")
else:
  print("=")
