a = int(input())
ma = a
mi = a
for i in range(4):
  x = int(input())
  if ma < x:
    ma = x
  elif mi > x:
    mi = x
if ma - mi <= int(input()):
  print("Yay!")
else:
  print(":(")