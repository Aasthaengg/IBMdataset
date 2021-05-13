def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n=int(input())
ar=lis()
from collections import Counter
C=Counter(ar)
s=sum(ar)
q=int(input())
for _ in range(q):
    b,c=sep()
    s-=(C[b]*(b-c))
    C[c]+=C[b]
    C[b]=0
    print(s)
