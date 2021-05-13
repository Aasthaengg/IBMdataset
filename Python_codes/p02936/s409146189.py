from collections import deque
n, q =map(int, input().split())

c=[0]*n

G = [[] for _ in range(n)]
for i in range(n-1):
    a,b=map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

for i in range(q):
    p, x=map(int, input().split())
    c[p-1] += x

ans = [0]*n

stack = deque()
stack.append([0, -1, 0])
while stack:
    v, parent, point = stack.pop()
    point += c[v]
    ans[v] = point
    for child in G[v]:
        if child == parent:
            continue
        stack.append([child, v, point])

print(*ans)