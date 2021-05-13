O = input()
E = input()
PASS = ''
if len(O)-len(E)==0:
  for i in range(len(O)):
   PASS += O[i]
   PASS += E[i]
else:
  for i in range(len(E)):
    PASS += O[i]
    PASS += E[i]
  PASS += O[-1]
print(PASS)