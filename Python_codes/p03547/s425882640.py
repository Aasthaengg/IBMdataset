X,Y=input().split()
L=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
if L.index(X)>L.index(Y):
  print(">")
elif L.index(X)<L.index(Y):
  print("<")
else:
  print("=")