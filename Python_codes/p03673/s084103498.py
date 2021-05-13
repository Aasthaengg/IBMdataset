import sys
from collections import deque


n = int(sys.stdin.readline().strip())
A = map(int, sys.stdin.readline().strip().split())

q = deque()
for i, a_i in enumerate(A):
    if i % 2 == 0:
        q.append(a_i)
    else:
        q.appendleft(a_i)

ans = list(map(str, q))
if n % 2 == 1:
    ans = ans[::-1]

print(" ".join(ans))