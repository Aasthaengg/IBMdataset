s=list(input())
n=len(s)
from collections import deque
q=deque([])

for i in range(n):
    if s[i]=='S':
        q.append('S')
    else:
        if q:
            if q[-1]=='T':
                q.append('T')
            else:
                q.pop()
        else:
            q.append('T')
print(len(q))