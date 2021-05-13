def dfs(u, cnt):
    cnt += point[u]
    counter[u] = cnt
    color[u] = GRAY
    for v in M[u]:
        if color[v] == WHITE:
            dfs(v, cnt)
    color[u] = BLACK

import sys
sys.setrecursionlimit(1000000)

n, q = map(int, input().split())
M = [[] for _ in range(n)]
point = [0] * n
for i in range(n-1):
    a, b = map(int, input().split())
    M[a-1].append(b-1)
    M[b-1].append(a-1)
for i in range(q):
    p, x = map(int, input().split())
    point[p-1] += x
#print(M, point)
    
WHITE, GRAY, BLACK = 0, 1, 2
color = [WHITE] * n

counter = [0] * n
dfs(0, 0)

print(*counter)
