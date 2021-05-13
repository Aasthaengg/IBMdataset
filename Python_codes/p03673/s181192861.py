from collections import deque
q=deque()

n=int(input())
a=input().split()
for i in range(n):
    if i%2==0:
        q.append(a[i])
    else:
        q.appendleft(a[i])

if n%2==0:
    print(' '.join(q))
else:
    print(' '.join(list(q)[::-1]))