from math import log2
n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
  if i>=k:p=1
  else:p=(1/2)**(int(log2((2*k-1)/i)))
  ans+=p/n
print(ans)