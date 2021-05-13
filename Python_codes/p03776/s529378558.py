from math import factorial
from collections import defaultdict
def nCr(n,r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))
N,A,B=map(int,input().split())
V=list(map(int,input().split()))
dict=defaultdict(int)
for i in V:
    dict[i]+=1
V.sort(reverse=True)
v=[]
value=0
tmp=0
for i in range(N):
    if value!=V[i]:
        tmp=1
        value=V[i]
    else:
        tmp+=1
    v.append([V[i],tmp])
ans=0
print(sum(V[:A])/A)
if V[0]==V[A-1]:
    for i in range(A,B+1):
        if V[0]==V[i-1]:
            ans+=nCr(dict[V[0]],i)
    print(ans)

else:
    print(nCr(dict[V[A-1]],v[A-1][1]))
