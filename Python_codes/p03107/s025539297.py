from collections import deque
S=input().strip()
N=len(S)

a=[0 if x == '0' else 1 for x in S]

q = deque()
for i in a:
    if q:
        if q[-1] != i:
            q.pop()
        else:
            q.append(i)
    else:
        q.append(i)

print(N-len(q))
