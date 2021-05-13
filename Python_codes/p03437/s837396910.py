X,Y = map (int, input ().split ())
if X < Y:
  print (X)
elif X == Y:
  print (-1)
else:
  if X%Y == 0:
    print (-1)
  else:
    print (X)