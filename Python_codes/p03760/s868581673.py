O=input()
E=input()
L=list()
for i in range(len(O)+len(E)):
  if i%2==0:
    L.append(O[i//2])
  else:
    L.append(E[(i-1)//2])
print("".join(L))