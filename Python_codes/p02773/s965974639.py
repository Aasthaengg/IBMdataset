n=int(input())
s=[input() for _ in range(n)]
from collections import Counter
c=Counter(s)
d=[]
x=c.most_common()[0][1]
for k in c.keys():
    if c[k]==x:
        d.append(k)

d.sort()
print(*d,sep='\n')