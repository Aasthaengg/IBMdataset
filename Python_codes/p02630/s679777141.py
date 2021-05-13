n=int(input())
a=list(map(int,input().split()))
from collections import Counter
C=Counter(a)
q=int(input())
s=sum(a)
for _ in range(q):
    b,c=map(int,input().split())
    s+=c*C[b]
    s-=b*C[b]
    print(s)
    C[c]+=C[b]
    C[b]=0
