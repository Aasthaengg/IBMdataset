from collections import deque
n, q = map(int, input().split())
queue = deque([input().split() for _ in range(n)])
t = 0
while len(queue):
    p = queue.popleft()
    if int(p[1]) <= q:
        t += int(p[1])
        print(p[0], t)
    else:
        p[1] = int(p[1]) - q
        t += q
        queue.append(p)