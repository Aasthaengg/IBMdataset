import heapq
INF = 10**10

def dijkstra(n, edges, s):
    """
    input
        n : 頂点数
        edges : リスト(始点, 終点, コスト)
        s : 始点
    output
        d : 始点からの最短距離
    """
    d = [INF] * n
    used = [False] * n
    d[s] = 0
    used[s] = True
    edgelist = []
    # 初期のやつ
    for v, c in edges[s]:
        # print("v{},c{}".format(v,c))
        # コストを前にしてpushしておく(そこから最小値を取り出すので)
        heapq.heappush(edgelist, (c, v))
    # 空になるまで
    while len(edgelist):
        # コスト最小値を取り出す
        c_min, v_min = heapq.heappop(edgelist)
        # そのエッジがすでに確定していたら終わり
        if used[v_min]:
            continue
        # 確定していなければ、そこから派生するエッジをコスト付与して与える
        d[v_min] = c_min
        used[v_min] = True
        for v, c in edges[v_min]:
            if not used[v]:
                heapq.heappush(edgelist, (c+c_min, v))
    return d
h,w = map(int, input().split())
cij = []
for i in range(10):
    row = list(map(int, input().split()))
    cij.append(row)
A = []
for i in range(h):
    row = list(map(int, input().split()))
    A.append(row)
edges = [[] for i in range(10)]
for i in range(10):
    for j in range(10):
        if i != j:
            edges[i].append((j, cij[i][j]))

ds = []
for i in range(10):
    costs = dijkstra(10,edges,i)
    ds.append(costs[1])
ans = 0
for r in A:
    for e in r:
        if e == -1: continue
        ans += ds[e]
print(ans)