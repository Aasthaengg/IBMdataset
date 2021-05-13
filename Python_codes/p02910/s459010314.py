S=input()
isOK=True
for i in range(len(S)):
  if((i+1)%2==1):
    if(S[i]=="L"):
      isOK=False
  else:
    if(S[i]=="R"):
      isOK=False
      
if(isOK):
  print("Yes")
else:
  print("No")
