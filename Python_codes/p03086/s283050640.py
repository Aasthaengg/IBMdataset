N=list(str(input()))
C=0
ans=0
for i in range(len(N)):
  if N[i]=="A" or N[i]=="C" or N[i]=="G" or N[i]=="T":
    C+=1
  else:
    C=0
  ans=max(ans,C)
print(ans)
