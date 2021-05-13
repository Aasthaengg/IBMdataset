K = int (input ())
A,B = map (int, input ().split ())
X = 'NG'
while A <= B:
  if A%K == 0:
    X = 'OK'
    break
  A += 1
print (X)