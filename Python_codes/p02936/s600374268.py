from collections import deque

n, q = map(int, input().split())
ab = [[] for _ in range(n)]
px = [0 for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    ab[a - 1].append(b - 1)
    ab[b - 1].append(a - 1)
for i in range(q):
    p, x = map(int, input().split())
    px[p - 1] += x

ans = px
queue = deque([(0, 0)])
while len(queue) > 0:
    prev, a = queue.pop()
    for c in ab[a]:
        if c != prev:
            ans[c] += ans[a]
            queue.append((a, c))

print(*ans)
