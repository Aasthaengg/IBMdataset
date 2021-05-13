import math
n,m=map(int,input().split())

if abs(n-m)>=2:
    ans=0
elif abs(n-m)==1:
    nper=math.factorial(n)%(10**9+7)
    mper=math.factorial(m)%(10**9+7)
    ans=(nper*mper)%(10**9+7)
else:
    nper=math.factorial(n)%(10**9+7)
    mper=math.factorial(m)%(10**9+7)
    ans=((nper*mper)*2)%(10**9+7)

print(ans)