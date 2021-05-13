from collections import deque

n, q = map(int, raw_input().split())
task = [raw_input().split() for _ in range(n)]

for t in task:
    t[1] = int(t[1])

Q = deque(task)
elaps = 0

while len(Q) > 0:
    u = Q.popleft()
    c = min(u[1], q)
    u[1] -= c
    elaps += c

    if u[1] > 0:
        Q.append(u)
    else:
        print u[0], elaps