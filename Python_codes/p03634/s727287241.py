import heapq
def dijkstra_heap(s,node_edges):
    '''
    ノードの入力は0-indexedに修正してから用いる
    returnはノードごとの最小コストを格納したリスト
    '''
    #始点sから各頂点への最短距離
    d = [float("inf")] * n
    used = [False] * n #True:未確定
    d[s] = 0
    used[s] = True
    edgelist = []
    # 始点がスタートになってるedgeをヒープキューに追加
    for e in node_edges[s]:
        heapq.heappush(edgelist,e)
    while len(edgelist):
        # ヒープキューからコスト最小のedgeをpop
        minedge = heapq.heappop(edgelist)
        # 該当edgeの行き先が確定済みになってなければこれを通って処理が続く
        if used[minedge[1]]:
            continue
        v = minedge[1]
        # 該当edgeの行き先のコストを更新
        d[v] = minedge[0]
        used[v] = True
        for e in node_edges[v]:
            if not used[e[1]]:
                heapq.heappush(edgelist,[e[0]+d[v],e[1]])
    return d

n = int(input())
node_edges = [[] for _ in range(n)]
for i in range(n-1):
    start, end, cost = map(int,input().split())
    start -= 1
    end -= 1
    node_edges[start].append([cost, end])
    node_edges[end].append([cost, start])
num_q, stop = map(int,input().split())
stop -= 1

dist_from_stop = dijkstra_heap(stop, node_edges)
ans_ls = [0] * num_q
for i in range(num_q):
    start, end = map(int,input().split())
    start -= 1
    end -= 1
    ans_ls[i] = dist_from_stop[start] + dist_from_stop[end]
for ans in ans_ls:
    print(ans)

