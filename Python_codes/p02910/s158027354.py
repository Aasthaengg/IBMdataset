a=input()
b=0
if (len(a))%2==0:
  for i in range(int(len(a)/2)):
    if a[2*i]=="R" or a[2*i]=="U" or a[2*i]=="D":
      b=b+1
    if a[2*i+1]=="L" or a[2*i+1]=="U" or a[2*i+1]=="D":
      b=b+1
  if b==len(a):
    print("Yes")
  else:
    print("No")
if (len(a))%2==1:
  for i in range(int(len(a)/2)+1):
    if a[2*i]=="R" or a[2*i]=="U" or a[2*i]=="D":
      b=b+1
  for i in range(int(len(a)/2)):
    if a[2*i+1]=="L" or a[2*i+1]=="U" or a[2*i+1]=="D":
      b=b+1
  if b==len(a):
    print("Yes")
  else:
    print("No")