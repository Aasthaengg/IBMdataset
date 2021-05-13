a=input()
b=input()
c=0
if (len(a)+1)!=len(b):
  print("No")
else:
  for i in range(len(a)):
    if a[i]==b[i]:
      c=c+1
  if c==len(a):
    print("Yes")
  else:
    print("No")