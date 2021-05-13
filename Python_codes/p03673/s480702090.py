from collections import deque
n = int(input())
a = list(map(int, input().split()))
Q = deque(a)
b = deque()
i = 1
while Q:
    q = Q.popleft()
    if i == 0:
        b.appendleft(q)
        i = 1
    else:
        b.append(q)
        i = 0
if n % 2 == 0:
    for bi in b:
        print(bi, end=' ')
    print('')
else:
    for bi in reversed(b):
        print(bi, end=' ')
    print('')