from collections import deque

n, q = (int(s) for s in input().split())

que = deque()
for i in range(n):
    name, ts = input().split()
    que.append((name, int(ts)))

t = 0
while que:
    name, time = que.popleft()
    if time <= q:
        t += time
        print(name, t)
    else:
        t += q
        que.append((name, time - q))