from collections import defaultdict
from sys import setrecursionlimit, getrecursionlimit

setrecursionlimit(100*getrecursionlimit())

N = int(input())
g = defaultdict(list)
K = []
for i in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    K.append((a,b))

C = sorted([int(i) for i in input().split()], reverse=True)

a = {i:0 for i in range(1, N+1)}

visited = defaultdict(bool)
ct = 0
def dfs(v):
    global ct
    visited[v] = True
    a[v] = C[ct]
    ct += 1
    for c in g[v]:
        if not visited[c]:
            dfs(c)

dfs(1)

ans1 = 0
ans2 = ' '.join([str(b) for b in a.values()])
for b, c in K:
    ans1 += min(a[b], a[c])

print(ans1)
print(ans2)