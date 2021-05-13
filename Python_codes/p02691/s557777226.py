# ABC166 
from collections import Counter

N=int(input())
A=[0]+list(map(int,input().split()))

Ai=[]
Aj=[]

for i in range(1,N+1):
    Ai.append(i+A[i])
    Aj.append(i-A[i])
    
ci=Counter(Ai).items()
cj=Counter(Aj)
res=0
for c,n in ci:
    m=cj[c]
    res+=m*n
print(res)

