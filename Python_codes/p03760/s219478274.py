O=input()
E=input()
s=''
for i in range(len(O)+len(E)):
  if i%2==0:
    s+=O[i//2]
    continue
  s+=E[i//2]
print(s)