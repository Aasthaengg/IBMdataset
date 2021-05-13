O=input()
E=input()

ans=""  
for i in range(len(O)):
  if len(O)-len(E)==0:
    ans=ans+(O[i]+E[i])
  elif len(O)-len(E)==1:
    if i<=len(E)-1:
      ans=ans+(O[i]+E[i])
    else:
      ans=ans+O[i]
print(ans)