n = int(input())
a = [int(input()) for _ in range(n)]
import sys

for i in range(n-1):
    if a[i+1] - a[i] >= 2:
        print(-1)
        sys.exit()
        
if a[0] != 0:
    print(-1)
    sys.exit()
    
a.append(1145141919810)
se = []
pl = [a[0]]
for i in range(n):
    if a[i+1] - a[i] == 1 or a[i+1] - a[i] == 0:
        pl.append(a[i+1])
    else:
        se.append(pl)
        pl = [a[i+1]]
        
from collections import Counter
ans = 0
for l in se:
    b = Counter(l)
    ans += max(l)
    for i in b:
        ans += max(0,b[i]-1) * i
        
print(ans)