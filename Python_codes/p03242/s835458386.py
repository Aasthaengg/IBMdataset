L=[0]*3
N=input()
for i in range(3):
  if N[i]=="1":
    L[i]=9
  else:
    L[i]=1
print((L[0]*100)+(L[1]*10)+L[2])