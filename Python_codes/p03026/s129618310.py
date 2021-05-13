from collections import deque 
n = int(input())
es = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    es[a - 1].append(b - 1)
    es[b - 1].append(a - 1)

c = list(map(int, input().split()))
c.sort()
print(sum(c) - c[-1])

d = [0] * n

q = deque([0])
d[0] = c.pop()

while q:
    v = q.popleft()
    for e in es[v]:
        if d[e]==0:
            d[e] = c.pop()
            q.append(e)
print(*d)