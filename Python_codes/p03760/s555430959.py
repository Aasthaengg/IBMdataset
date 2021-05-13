O=input()
E=input()
res = ""
for i in range(len(E)):
  res += O[i]+E[i]
if len(O)-len(E) == 1:
  res += O[len(O)-1]
print(res)