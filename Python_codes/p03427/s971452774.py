n=input()
l=len(n)
if all(n[i]=="9" for i in range(1,l)):
  print(int(n[0])+9*(l-1))
else:
  print(int(n[0])-1+9*(l-1))