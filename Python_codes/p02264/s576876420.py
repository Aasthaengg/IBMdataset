from collections import deque
n, q = map(int, input().split())
queue = deque()
for _ in range(n):
    name, time = input().split()
    queue.append((name, int(time)))

comp = []
t = 0
while queue:
    name, time = queue.popleft()
    if time <= q:
        t += time
        comp.append((name, t))
    else:
        t += q
        queue.append((name, time - q))
for s in comp:
    print(*s)
