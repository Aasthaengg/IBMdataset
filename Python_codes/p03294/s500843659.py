n=int(input())
a=list(map(int,input().split()))
import fractions
ans=0
m=a[0]
for i in range(1,n):
  m=(m*a[i])//fractions.gcd(m,a[i])
for i in range(n):
  ans=ans+(m-1)%a[i]
print(ans)