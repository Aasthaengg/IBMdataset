A,B,C = map(int, input ().split ())
X = A%B
if X == C:
  print ('YES')
else:
  i = 2
  while True:
    x = (i*A)%B
    if x == C:
      print ('YES')
      break
    elif x == X:
      print ('NO')
      break
    i += 1