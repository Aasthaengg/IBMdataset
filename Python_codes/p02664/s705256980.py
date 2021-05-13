T=input()
S=""
if T[0]=="?":
  S+="D"
else:
  S+=T[0]
for x in range(1,len(T)):
  if T[x]=="?":
    S+="D"
  else:
    S+=T[x]
print(S)