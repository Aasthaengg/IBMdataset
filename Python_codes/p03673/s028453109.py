from collections import deque
n=int(input())
a=list(map(int,input().split()))
b=deque()
for i in range(n):
    if i%2==0:
        b.append(a[i])
    if i%2==1:
        b.appendleft(a[i])

if n%2==1:
    c=deque()
    for i in range(n):
        d=b.pop()
        c.append(d)
    print(*c)
else:
    print(*b)

