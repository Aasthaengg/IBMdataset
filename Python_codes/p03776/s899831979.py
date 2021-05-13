from statistics import mean
from collections import Counter
n,a,b=map(int,input().split())
v=sorted(list(map(int,input().split())),reverse=True)
avg=mean(v[:a])
print(avg)

p=Counter(v[:a])[v[a-1]]
q=Counter(v)[v[a-1]]

def n_func(n):
    ans=1
    for i in range(1,n+1):ans=(ans*i)
    return ans

def nCr(n,r):
    return (n_func(n)//n_func(r))//n_func(n-r)

if v[0]==v[a-1]:
    print(sum([nCr(q,a+i) for i in range(0,min(b,q)-a+1)]))
else:
    print(nCr(q,p))