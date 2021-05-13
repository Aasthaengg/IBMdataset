import math

S = list(input())
a =0
b = 0
n=len(S)
for i in range(0,n,2):
  if(S[i]=="R" or S[i]=="U" or S[i]=="D"):
    a +=1
for j in range(1,n,2):
  if(S[j]=="L" or S[j]=="U" or S[j]=="D"):
    b+=1
if(a==math.ceil(n/2) and b ==math.floor(n/2)):
  print("Yes")
else:
  print("No")