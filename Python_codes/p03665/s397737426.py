n,p=map(int,input().split())
a=list(map(int,input().split()))
even=0
odd=0
for i in a:
    if i%2==0:
        even+=1
    else:
        odd+=1
import math
ans=2**even
if p==0:
    m=odd//2
    t=1
    for i in range(1,m+1):
        i*=2
        t+=math.factorial(odd)/math.factorial(i)/math.factorial(odd-i)
else:
    m=(odd+1)//2
    t=0
    for i in range(1,m+1):
        i=2*i-1
        t+=math.factorial(odd)/math.factorial(i)/math.factorial(odd-i)
ans*=t
print(int(ans))