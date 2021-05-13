n,a,b=map(int,input().split())
v=[int(i) for i in input().split()]
v.sort()
v.reverse()
ans=0
from collections import Counter
c=Counter()
k=0
tmp=0
for i in range(n):
    if i<a-1:
        ans+=v[i]
        c[v[i]]+=1
    elif i==a-1:
        tmp=v[i]
        c[v[i]]+=1
        ans+=v[i]
    else:
        if tmp!=v[i]:
            break
        else:
            c[v[i]]+=1
            k+=1
ans=ans/a
print(ans)
def f(n,m):
    import math
    if n-m<0:
        return 0
    return(math.factorial(n)//math.factorial(n-m)//math.factorial(m))
ans2=0

if ans==tmp:
    for i in range(c[tmp]-k,c[tmp]-k+b-a+1):
        ans2+=f(c[tmp],i)
    print(ans2)
else:
    print(f(c[tmp],k))


