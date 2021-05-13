n = int(input())
a = list(map(int, input().split()))

from collections import deque

d = deque()
for i,num in enumerate(a):
    if i&1:
        d.appendleft(num)
    else:
        d.append(num)

if n&1:
    d.reverse()

print(*d)