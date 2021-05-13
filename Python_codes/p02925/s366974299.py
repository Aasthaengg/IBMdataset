from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = [deque(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
ans = 0
used_prev = set(range(N))
while any(A):
    used = set()
    for i in used_prev:
        if not A[i] or i in used:
            continue
        j = A[i][0]
        if j in used:
            continue
        if A[j][0] == i:
            used.add(i)
            used.add(j)
            A[i].popleft()
            A[j].popleft()
    if not used:
        ans = -1
        break
    used_prev = used
    ans += 1
print(ans)
