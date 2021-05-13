import math
a,b = map(int,input().split())
ans=-1
for i in range(math.ceil(a*12.5),math.ceil(12.5*(a+1))-1):
  if i//10==b:
    ans=i
    break
print(ans)