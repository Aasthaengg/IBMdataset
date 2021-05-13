N = list(map(int, input().split())) 
R = N[0]-2*N[1]
if R <= 0:
  print (0)
else:
  print (R)