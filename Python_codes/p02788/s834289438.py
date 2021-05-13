from collections import deque
from math import ceil

n,d,a = map(int,input().split())
xh = sorted([list(map(int,input().split())) for _ in range(n)])

q = deque()
ans = 0
count = 0
total = 0
for x,h in xh:
    while q:
        if q[0][0] < x:
            total -= q.popleft()[1]
        else:
            break
    
    if total < ceil(h/a):
        count = ceil(h/a)-total
        ans += count
        total += count
        q.append((x+2*d,count))

print(ans)