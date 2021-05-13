import math
n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
  if i>=k:
    ans+=1/n
    continue
  x=(1/n)*pow(2,-1*math.ceil(math.log2(k/i)))
  ans+=x
print(ans)