N = int (input ())
D,X = map (int, input ().split ())
c = 0
for i in range (N):
  A = int (input ())
  c += 1+(D-1)//A
print (c+X)