import sys
N = int(input())
G = [{} for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    G[u][v] = w
    G[v][u] = w

ans = [0] * N
todo = [(0, 0)]
done = set()
while todo:
    p, d = todo.pop()
    for np, dd in G[p].items():
        if not np in done:
            nd = d + dd
            ans[np] = nd % 2
            todo.append((np, nd))
    done.add(p)

for x in ans:
    print(x)