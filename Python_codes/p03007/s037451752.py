N = int(input())
A = list(map(int,input().split()))
A.sort()

from collections import deque
q = deque(A)
mn = q.popleft()
mx = q.pop()

arr = []
for a in q:
    if a >= 0:
        arr.append((mn, a))
        mn -= a
    else:
        arr.append((mx, a))
        mx -= a
arr.append((mx, mn))
print(mx - mn)
for a,b in arr:
    print(a,b)