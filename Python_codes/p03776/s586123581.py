from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n,a,b=map(int,input().split())
v=list(map(int,input().split()))
v.sort(reverse=True)
ans=0
for i in range(a):
    ans+=v[i]
ans/=a
print(ans)
if v[0]==v[a-1]:
    count=0
    for i in range(n):
        if v[i]==v[0]:
            count+=1
    cnt=0
    for i in range(a,min(b,count)+1):
        cnt+=cmb(count,i)
    print(cnt)
else:
    count=0
    for i in range(n):
        if v[i]==v[a-1]:
            count+=1
    for i in range(n):
        if v[i]==v[a-1]:
            l=i
            break
    cnt=cmb(count,a-l)
    print(cnt)