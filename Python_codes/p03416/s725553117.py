A,B = map (int, input ().split ())
x = 0
while A <= B:
  if int(str(A)[0])==int(str(A)[4]) and int(str(A)[1])==int(str(A)[3]):
    x += 1
  A += 1
print (x)