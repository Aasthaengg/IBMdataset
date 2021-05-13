n,m=(int(i) for i in input().strip().split(" "))
ar=[int(i)%m for i in input().strip().split(" ")]
t=[0,ar[0]]
for i in range(1,n):
    t.append((t[i]+ar[i])%m)
from collections import Counter
c=Counter(t)
ans=0
for i in c.values():
    ans+=((i*(i-1))//2)
print(ans)
