x=int(input())
flag=False
for a in range(121):
  for b in range(-121,121):
    if(a**5-b**5==x):
      flag = True
      break
  if(flag==True):
    break
print(a,b)