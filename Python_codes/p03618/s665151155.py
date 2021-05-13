s=input()
from collections import Counter
c=Counter(s)
m=0
for k in c.values():
    m+=k*(k-1)//2
n=len(s)
print(n*(n-1)//2-m+1)
