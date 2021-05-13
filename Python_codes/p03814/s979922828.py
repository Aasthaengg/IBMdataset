S=input()

i=0
A=[]
Z=[]
for s in S:
  if s=="A":
    A.append(i)
  elif s=="Z":
    Z.append(i)
  i=i+1
  
print(max(Z)+1-min(A))

