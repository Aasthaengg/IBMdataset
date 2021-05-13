O=input()
E=input()
P = ""
for i in range(len(E)):
  P += O[i]
  P += E[i]
if len(O)-len(E)==1:
  P += O[-1]
print(P)