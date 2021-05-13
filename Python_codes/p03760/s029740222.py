O = input()
E = input()
A = ""
for x,y in zip(O,E):
  A += x + y
if len(O) == len(E):
  print(A)
else:
  print(A + O[-1])