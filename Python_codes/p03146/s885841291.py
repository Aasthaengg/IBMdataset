s=int(input())

if s==1 or s==2 or s==4:
  cnt=0
else:
  cnt=0
  while s!=4:
    if s%2==0:
      s=s/2
      cnt+=1
    else:
      s=3*s+1
      cnt+=1 

print(cnt+4)