
from collections import defaultdict
d=set()
a=defaultdict(list)
n = int(input())
for i in range(n):
    h,m=list(map(int,input().split()))
    a[m].append(h)
    d.add(m)
t=0
r=0

for i in sorted(d):
    for j in a[i]:
        t+=j
    if t>i:
        r=1
        break
if r==1:
    print('No')
else:
    print('Yes')