import sys
sys.setrecursionlimit(10**9)

N = int(input())
edge = [[] for _ in range(N)]
cnt = [[0,i] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append(b)
    edge[b].append(a)
    cnt[a][0] += 1
    cnt[b][0] += 1


cnt.sort(reverse=True)
start = cnt[0][1]
C = list(map(int, input().split()))
C.sort(reverse=True)
nodes = [0] * N

#print(nodes)
cidx = -1
ans = []
def dfs(v, pv, w):
    global cidx
    cidx += 1
    nodes[v] = C[cidx]
    ans.append(min(w, C[cidx]))
    for nv in edge[v]:
        if pv == nv: continue
        dfs(nv, v, C[cidx])

dfs(start, 0, 0)
print(sum(ans))
print(*nodes, sep=" ")
