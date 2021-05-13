import sys
sys.setrecursionlimit(10**5 + 5)
N, M = map(int, input().split())
H = [0] + list(map(int, input().split()))
Graph = [[] for _ in range(N+1)]
is_good = [False] + [True] * N
seen = [True] + [False] * N

def dfs(cur):
    global Graph, seen, H
    seen[cur] = True
    for nex in Graph[cur]:
        if H[nex] >= H[cur]:
            is_good[cur] = False
        if seen[nex]:
            continue
        dfs(nex)


for _ in range(M):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)

for i in range(1, N+1):
    if not seen[i]:
        dfs(i)

print(is_good.count(True))