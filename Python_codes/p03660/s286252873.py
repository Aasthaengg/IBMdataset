from collections import deque

def bfs(i, c):
    q = deque()
    q.append(i)
    while q:
        p = q.popleft()
        for j in g[p]:
            if c[j] == 0 and i != j:
                q.append(j)
                c[j] = c[p] + 1
    return c

n = int(input())
g = [-1] * n
c1 = [0] * n
c2 = [0] * n
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if g[a] == -1:
        g[a] = [b]
    else:
        g[a].append(b)
    if g[b] == -1:
        g[b] = [a]
    else:
        g[b].append(a)

c1 = bfs(0, c1)
c2 = bfs(n - 1, c2)

F, S = 0, 0
for i in range(n):
    if c1[i] <= c2[i]:
        F += 1
    else:
        S += 1
print("Fennec" if F > S else "Snuke")