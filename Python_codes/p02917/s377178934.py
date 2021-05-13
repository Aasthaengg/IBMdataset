n=int(input())
b=list(map(int,input().split()))
if len(b)==1:
  print (2*b[0])
else:
  ans=0
  for i in range(1,len(b)):
    ans+=min(b[i],b[i-1])
  print (ans+b[0]+b[len(b)-1])