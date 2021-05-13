N=input()
N=list(str(N))
le=-1
ri=-1
for i in range(len(N)):
  if N[i]=="A":
    le=i
    break
for k in range(len(N)):
  if N[k]=="Z":
    ri=k
print(ri-le+1)

