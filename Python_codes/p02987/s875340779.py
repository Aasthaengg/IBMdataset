S=input()
isOK=True
for i in range(4):
  if(S.count(S[i])!=2):
    isOK=False
if(isOK):
  print("Yes")
else:
  print("No")