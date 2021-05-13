n,k=map(int,input().split())
l=tuple(map(int,input().split()))
a=sum(l)
ans=1
def f(i):
    p=[]
    for j in l:
        r=j%i
        if r:p.append(r)
    p.sort()
    a=i*len(p)-sum(p)
    now=0
    for j in p:
        now+=j
        a-=i-j
        if now<=k and a<=k and abs(now-a)%i==0:
            return i
    return 0

from math import floor,sqrt
for i in range(1,floor(sqrt(a))+1):
    if a%i==0:
        ans=max(f(i),ans,f(a//i))

print(ans)