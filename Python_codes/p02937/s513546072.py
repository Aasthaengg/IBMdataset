#138-e
from collections import defaultdict
import bisect

s = input()
t = input()
n = len(s)
m = len(t)

ans=0
pos=-1

d = defaultdict(list)
for i in range(n):
    if s[i] in t:
        d[s[i]].append(i)
        
for i in range(n):
    if s[i] in t:
        d[s[i]].append(i+n)
        
for v in t:
    l = d[v]
    ind = bisect.bisect_right(l, pos)
    if l:
        ans += l[ind]-pos
        if l[ind]<n:
            pos = l[ind]
        else:
            pos = l[ind] - n
    else:
        ans = -1
        break
        
print(ans)
        

