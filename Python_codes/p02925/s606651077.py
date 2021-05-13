N = int(input())
A = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N)]

indices = [0] * N
def next(i):
    return A[i][indices[i]] if indices[i] < N-1 else -1

from collections import deque
q = deque()
for i in range(N):
    j = next(i)
    if i < j and next(j) == i:
        q.append((i, j))

m = N*(N-1)//2
days = 0
while q:
    days += 1
    nq = deque()
    while q:
        i, j = q.pop()
        m -= 1
        indices[i] += 1
        indices[j] += 1
        ni = next(i)
        nj = next(j)
        if ni >= 0 and next(ni) == i:
            nq.append((i, ni))
        if nj >= 0 and nj != i and next(nj) == j:
            nq.append((j, nj))
    q = nq

if m > 0:
    print(-1)
else:
    print(days)
