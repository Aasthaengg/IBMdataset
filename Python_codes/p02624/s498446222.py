import math
n=int(input())
ans=0
for i in range(1,n+1):
    a=i
    d=i
    k=n//i
    ans+=k*(2*a+(k-1)*d)//2
print(ans)