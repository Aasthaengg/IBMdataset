n=int(input())
a=list(map(int,input().split()))
a.sort()
s=[0]
si=0
for ai in a:
    si+=ai
    s.append(si)
import bisect
ans=0
#色iにたいして2xAi以下の
for ai in a:
    b0=0
    b1=1
    c=ai
    while b0!=b1:
        b0=b1
        b1=bisect.bisect_right(a,2*c)
        c=s[b1]
    if b1==n:
        ans+=1
print(ans)


