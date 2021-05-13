import math
MOD=1000000007
N=int(input())
f=[0]*1000

def factors(n):
  for i in range(2,n+1):
    if n==1: return
    if n%i==0:
      while n%i==0:
        f[i]+=1
        n//=i

for i in range(2,N+1):
  factors(i)

ans=1
for i in range(1000):
  if f[i]>0:
    ans*=(f[i]+1)
    ans%=MOD

print(ans)
