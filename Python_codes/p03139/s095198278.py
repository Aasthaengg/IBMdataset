N,A,B = map (int, input ().split ())
if A < B:
  x = A
else:
  x = B
if A+B-N < 0:
  y = 0
else:
  y = A+B-N
print (x,y)