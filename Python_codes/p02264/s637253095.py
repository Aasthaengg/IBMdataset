from collections import deque

n, q = map(int, input().split())
p = deque()
for i in range(n):
    name, t = input().split()
    time = int(t)
    p.append((name, time))
elapsed = 0
while len(p) > 0:
    name, time = p.popleft()
    elapsed += min(q, time)
    if time > q:
        p.append((name, time - q))
    else:
        print(name, elapsed)

