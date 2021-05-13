n,m = map(int,input().split())
from collections import Counter

s = []
for _ in range(m):
    a,b = map(int,input().split())
    s.append(a)
    s.append(b)
    
c = Counter(s)
d = list(c.values())

ans = "YES"
for i in d:
    if i % 2 == 1:
        ans = "NO"
        break
        
print(ans)