n,k = map(int,input().split())
from collections import deque
l = [[] for _ in range(n)]
for i in range(n-1):
    ta,tb = map(int,input().split())
    l[ta-1].append(tb-1)
    l[tb-1].append(ta-1)
c,q = k,deque([0])

while q:
    v,i = q.pop(),1
    for w in l[v]:
        c = c*(k-i-(v>0))%(10**9+7)
        l[w].remove(v)
        q.append(w)
        i+=1
print(c)

