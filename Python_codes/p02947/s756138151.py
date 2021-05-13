n=int(input())
arr=[]
from collections import Counter
c=Counter([])
for _ in range (n):
    s=input()
    z=[item for item in s]
    z.sort()
    z=tuple(z)
    c[z]+=1
ans=0
for item in c.values():
    ans+=(item*(item-1))//2
print (ans)