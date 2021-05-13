n,m = list(map(int, input().split()))
from collections import defaultdict
d=defaultdict(list)
for _ in range(m):
    a,b = list(map(int, input().split()))
    d[a].append(b)
    d[b].append(a)
ans=[0]*n
for k in d:
    ans[k-1]=len(d[k])
print(*ans, sep='\n')