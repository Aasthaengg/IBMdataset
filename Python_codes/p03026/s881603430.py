N = int(input())
from collections import deque
e = []
for i in range(N-1):
    a,b = map(int,input().split())
    e.append((min(a,b)-1,max(a,b)-1))
e.sort()
e = deque(e)
c = list(map(int,input().split()))
c.sort()
print(sum(c)-c[-1])

d = [0]*N
d[0] = str(c.pop())
while e:
    a,b = e.popleft()
    if d[a] != 0 and d[b] == 0:
        d[b] = str(c.pop())
    elif d[a] == 0 and d[b] != 0:
        d[a] = str(c.pop())
    else:
        e.append((a,b))

print(' '.join(d))