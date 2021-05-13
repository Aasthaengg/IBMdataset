from collections import deque

n, m = map(int, input().split())
l = [[] for _ in range(n + 1)]

for i in range(1, m + 1):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

q = deque([1])
s = [1] + [0] * n

while q:
    u = q.popleft()
    for v in l[u]:
        if not s[v]:
            s[v] = u
            q.append(v)
print('Yes')

for i in range(2, n + 1):
    print(s[i])