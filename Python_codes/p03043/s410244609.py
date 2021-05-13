import math
n,k=map(int, input().split())
ans=0
for i in range(1,n+1):
  if i>=k:
    ans+=1/n
  else:
    ans+=0.5**math.ceil(math.log2(k/i))/n
print(ans)