import sys
from collections import deque

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))

res = deque()
t = (N + 1) % 2

for i in range(N):
    if i % 2 == t:
        res.appendleft(A[i])
    else:
        res.append(A[i])

print(*res)
