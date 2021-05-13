from collections import deque

N = int(input())
a =list(map(int,input().split()))

d = deque()

for i in range(N):
    if i % 2 == 0:
        d.append(a[i])
    else:
        d.appendleft(a[i])

if N % 2 != 0:
    d.reverse()
print(*d)