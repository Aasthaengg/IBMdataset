X,Y = input().split()

ABC=["A", "B", "C","D", "E", "F"]
if ABC.index(X)>ABC.index(Y):
  print('>')
elif ABC.index(X)==ABC.index(Y):
  print('=')
else:
  print('<')