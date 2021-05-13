import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
edges = [[]for _ in range(n)]
for _ in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)
INF = 10**18
dist = [INF]*n
dist[0] = 0
prev = [None]*n


def dfs(v, parent, d):
    prev[v] = parent
    dist[v] = d
    for v2 in edges[v]:
        if v2 == parent:
            continue
        dfs(v2, v, d+1)


dfs(0, -1, 0)

x = n-1
for _ in range((dist[-1]-1)//2):
    x = prev[x]
cant_go = prev[x]


def dfs2(v, parent):
    global snuke_v_cnt
    snuke_v_cnt += 1
    for v2 in edges[v]:
        if v2 == parent:
            continue
        if v2 == cant_go:
            continue
        dfs2(v2, v)


snuke_v_cnt = 0
dfs2(x, -1)

fennec_v_cnt = n-snuke_v_cnt
print('Fennec' if snuke_v_cnt < fennec_v_cnt else 'Snuke')