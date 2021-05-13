import sys
sys.setrecursionlimit(200000)

N, M, P = map(int, input().split())

INF = 10**10
# Bellman-Fordをするときは、辺集合を持つ
edges = [] 
# 1から行けない辺やNに到達できない辺を削除するための探索をする用
to = [[] for _ in range(2505)]
rto = [[] for _ in range(2505)]
reachableFrom1 = [False for _ in range(2505)]
reachableToN = [False for _ in range(2505)]
ok = [False for _ in range(2505)]

def dfs(v):
    if reachableFrom1[v]:
        return
    reachableFrom1[v] = True
    for u in to[v]:
        dfs(u)

def rdfs(v):
    if reachableToN[v]:
        return
    reachableToN[v] = True
    for u in rto[v]:
        rdfs(u)

for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    c -= P
    c = -c # 最短路にするため符号を逆転
    edges.append([a, b, c])
    to[a].append(b)
    rto[b].append(a)

# 考えるべき頂点だけ洗い出し
dfs(0)
rdfs(N-1)
for i in range(N):
    ok[i] = reachableFrom1[i] & reachableToN[i]

# Bellman-Ford
d = [INF for _ in range(N)]
d[0] = 0
upd = True
step = 0
flag = True
while upd:
    upd = False
    for i in range(M):
        a, b, c = edges[i]
        if not ok[a]:
            continue
        if not ok[b]:
            continue
        newD = d[a]+c
        if newD < d[b]:
            upd = True
            d[b] = newD
    step += 1
    if step > N:
        flag = False
        break
if flag:
    ans = -d[N-1]
    ans = max(ans, 0)
    print(ans)
else:
    print(-1)