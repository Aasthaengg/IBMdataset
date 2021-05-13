a=int(input())
ct=1
if a==1:
  print(4)
  exit()
elif a==2:
  print(4)
  exit()
while a!=1:
  ct+=1
  if a%2==0:
    a=a//2
  else:
    a=3*a+1
else:
  ct+=1
  print(ct)
