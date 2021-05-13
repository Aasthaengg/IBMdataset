s=input()
t=input()
l1=list(s)
l2=list(t)
c=0
if l1==l2:
  print(3)
else:
  for i in range(len(l1)):
    if l1[i]==l2[i]:
      c+=1
  print(c) 