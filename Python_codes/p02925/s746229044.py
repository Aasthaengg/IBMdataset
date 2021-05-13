import sys
from collections import deque

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
A = [deque([(i, x) for x in lr()]) for i in range(1, N+1)]
day = 0
candidate = {A[i][0] for i in range(N)}
match = 0

while candidate:
    day += 1
    used = set()
    next = set()
    for a, b in candidate:
        if a in used or b in used:
            continue
        if A[b-1][0] == (b, a):
            match += 1
            A[a-1].popleft()
            A[b-1].popleft()
            if A[a-1]:                
                next.add(A[a-1][0])
            if A[b-1]:
                next.add(A[b-1][0])
            used.add(a)
            used.add(b)
    if match == N * (N-1) // 2:
        break
    candidate = next
    if not used:
        print(-1); exit()

print(day)
#
