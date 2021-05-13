n,k=[int(x) for x in input().rstrip().split()]
a=[int(x) for x in input().rstrip().split()]
now=0
ans=0
if n==k:
  print(1)
else:
  while(True):
    n-=k
    ans+=1
    if n<=0:
      break
    else:
      n+=1
      
  print(ans)