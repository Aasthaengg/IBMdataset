O=input()
E=input()
for i in range(0,len(E)):
  print(O[i],end="")
  print(E[i],end="")
if len(O)!=len(E):
  print(O[-1],end="")
