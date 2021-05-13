
n,m,q=(int(i) for i in input().strip().split(" "))
from collections import defaultdict
d=defaultdict(int)
for _ in range(m):
    a,b=(int(i) for i in input().strip().split(" "))
    d[(a,b)]+=1
for i in range(1,n+1):
    for j in range(1,n+1):
        d[(i,j)]+=d[(i,j-1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        d[(i,j)]+=d[(i-1,j)]

for i in range(q):
    l,r = (int(i) for i in input().strip().split(" "))
    print(d[(r,r)]+d[(l-1,l-1)]-d[(l-1,r)]-d[(r,l-1)])
