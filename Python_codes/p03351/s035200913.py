a,b,c,d=map(int,input().split())
disAC = abs(c-a)
disAB = abs(b-a)
disBC = abs(c-b)
if disAC <= d:
  print("Yes")
elif disAB <= d and disBC <= d:
  print("Yes")
else:
  print("No")