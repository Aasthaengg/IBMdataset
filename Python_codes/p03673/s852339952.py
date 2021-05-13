from collections import deque

n = int(input())
A = list(input().split())
a = [int(A[i]) for i in range(n)]

b = deque([])
b_rev = deque([])

for i in range(n):
    if i % 2 == 0:
        b.append(str(A[i]))
        b_rev.appendleft(str(A[i]))
    else:
        b.appendleft(str(A[i]))
        b_rev.append(str(A[i]))
    
if n % 2 == 0:
    print(' '.join(b))
else:
    print(' '.join(b_rev))