n,a,b=map(int,input().split())
if a+b-n>0:
  ans=a+b-n
else:
  ans=0
print(min(a,b),ans,sep=' ')
