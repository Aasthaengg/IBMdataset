import sys
input = sys.stdin.buffer.readline

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)
C = list(map(int, input().split()))
C.sort()

s = []
parent = [-1]*n
order = []
s.append(0)
while s:
    v = s.pop()
    order.append(v)
    for u in g[v]:
        if parent[v] == u:
            continue
        parent[u] = v
        s.append(u)

order.reverse()
ans = 0
D = [0]*n
for i in range(n):
    v = order[i]
    D[v] = C[i]
    if i != n-1:
        ans += C[i]
print(ans)
print(*D)
