import math
n,k=map(int,input().split())
ans=0
t=n
for i in range(1,n+1):
    t=i
    p=1/n
    while t<k:
        p=p*(1/2)
        t=t*2
    ans+=p
print(ans)