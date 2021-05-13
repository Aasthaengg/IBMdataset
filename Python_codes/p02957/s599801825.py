A,B = map (int, input ().split ())
X = (A+B)/2
if X%1 == 0:
  print (round(X))
else:
  print ('IMPOSSIBLE')