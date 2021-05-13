from collections import deque
N = int(input())
A = list(map(int,input().split()))

b = deque()
for i,a in enumerate(A):
    if i%2:
        b.appendleft(a)
    else:
        b.append(a)

if N%2:
    print(*reversed(b))
else:
    print(*b)