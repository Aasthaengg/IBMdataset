s=input()
cont=0
for i in range(0,len(s),2):
  if s[i]=="L":
    print("No")
    cont+=1
    break
for j in range(1,len(s),2):
  if s[j]=="R" and cont==0:
    print("No")
    cont+=1
    break
if cont==0:
    print("Yes")