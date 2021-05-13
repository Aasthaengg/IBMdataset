from collections import deque
n=int(input())
a=list(map(int,input().split()))
head=False
d = deque()
for i in range(n):
    if head==True:
        d.appendleft(a[i])
    else:
        d.append(a[i])
    head = not head
if head==True:
    d=list(d)
    print(*d[::-1])
else:
    print(*d)