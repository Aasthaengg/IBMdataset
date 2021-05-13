A,B,C = map (int, input ().split ())
X = A-B
Y = C-X
if Y < 0:
  print (0)
else:
  print (Y)