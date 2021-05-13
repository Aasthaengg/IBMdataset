s=int(input())
if s==1 or s==2:
  print(4)
else:
  i=1
  while s!=1:
    i+=1
    if s%2==0:
      s/=2
    else:
      s=s*3+1
  print(i+1)
