N = int(input())
A = list(map(int,input().split()))
from collections import deque
b = deque()
for i in range(N):
    if i%2==0:
        b.append(A[i])
    else:
        b.appendleft(A[i])
out = list(b)
if N%2==0:
    print(*out)
else:
    print(*out[::-1])
