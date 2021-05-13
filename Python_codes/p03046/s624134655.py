from collections import deque

m, k = [int(i) for i in input().split()]

if k >= 2 ** m:
    print(-1)
    exit()

if k == 0:
    q = deque([])
    for i in range(2 ** m):
        q.append(i)
        q.appendleft(i)
    print(*q)
    exit()

if m == 1 and k == 1:
    print(-1)
    exit()

S = set(i for i in range(2 ** m))

q = deque([0, k])
S.remove(0)
S.remove(k)

for s in S:
    q.appendleft(s)
    q.append(s)

q.appendleft(0)
q.append(k)

print(*q)
