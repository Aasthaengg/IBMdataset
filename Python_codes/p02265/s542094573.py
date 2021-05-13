from collections import deque
from sys import stdin
q = deque()
input()
for s in stdin:
    if s == '\n':
        break
    c, *k = s.split()
    k = k[0] if k else None
    if c == 'insert':
        q.appendleft(k)
    elif c == 'delete':
        if k in q:
            q.remove(k)
    elif c == 'deleteFirst':
        q.popleft()
    else:
        q.pop()
print(*q)
