import collections
import sys
n = int(input())
ls = list(map(int,input().split()))
c =collections.Counter(ls)
d = list(c)
p = []
q = []
mm = 0
mx3 = 0
for i in range(len(d)):
    if c[d[i]] >=4:
        p.append(d[i])
    if c[d[i]] >=2:
        q.append(d[i])
if p == [] and len(q) < 2:
    print(0)
    sys.exit()
if len(q) >= 2:
    mx1 = max(q)
    q.remove(mx1)
    mx2 = max(q)
    mm = mx1 * mx2
if p != []:
    mx3 = max(p)**2
print(max(mm,mx3))
    

