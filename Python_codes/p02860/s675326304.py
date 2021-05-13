c=input()
c=int(c)
a=input()
b=0
if c%2==1:
  print("No")
else:
  for i in range(int(c/2)):
    if a[i]!=a[i+int(c/2)]:
      b=b+1
  if b==0:
    print("Yes")
  else:
    print("No")