from math import factorial
from collections import Counter

n,a,b=map(int,input().split())
v=sorted(list(map(int,input().split())),reverse=True)

ma=sum(v[:a])/a
print(ma)
cnt=Counter(v)

if v[a-1]==v[0]:
    m=cnt[v[0]]
    ans=0
    for i in range(a,min(b,m)+1):
        ans+=factorial(m)//(factorial(i)*factorial(m-i))
    
    print(ans)
else:
    m=cnt[v[a-1]]
    r=Counter(v[:a])[v[a-1]]

    print(factorial(m)//(factorial(r)*factorial(m-r)))
