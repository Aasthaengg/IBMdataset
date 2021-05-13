from collections import deque
from sys import stdin
q = deque()
input()
for s in stdin:
    c, *k = s.split()
    k = k[0] if k else None
    if c[0] == 'i':
        q.appendleft(k)
    elif c[0] == 'd':
        if c[6:7] == 'F':
            q.popleft()
        elif c[6:7] == 'L':
            q.pop()
        else:
            if k in q:
                q.remove(k)
print(*q)
