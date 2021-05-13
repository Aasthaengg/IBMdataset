n=int(input())
a=[0]*n
b=[0]*n
import math
ans=0
for i in range(n):
  a[i],b[i]=map(int,input().split())
for i in range(n-1,-1,-1):
  ans+=b[i]*(math.ceil((ans+a[i])/b[i]))-a[i]-ans
print(ans)