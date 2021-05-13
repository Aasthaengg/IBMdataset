A = input ()
B = input ()
C = input ()
X,Y,Z = 0,0,0
P = A
Q = X
while True:
  if len(P)==Q:
    if P==A:
      print ('A')
    elif P==B:
      print ('B')
    else:
      print ('C')
    break
  if P==A:
    X += 1
  elif P==B:
    Y += 1
  else:
    Z += 1
  if P[Q]=='a':
    P = A
    Q = X
  elif P[Q]=='b':
    P = B
    Q = Y
  else:
    P = C
    Q = Z