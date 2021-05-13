def dijkstra_list(graph, startidx):
    # 頂点数
    n_nodes = len(graph)
    
    # 各頂点の情報
    nodes = []
    for i in range(n_nodes):
        nodes.append([
            float("inf"), # cost
            None,         # from
            False,        # 確定したか？
            i             # 自分自身の頂点番号(0-indexed)、nodesのindexと一致するはず
        ])

    # 優先度付きキューの準備
    import heapq
    priority_queue = []
    heapq.heapify(priority_queue)

    # 初期化
    nodes[startidx][0] = 0
    nodes[startidx][1] = None
    nodes[startidx][2] = True

    # 始点から到達できるnodeを優先度付きキューに入れる
    for dst, cost in graph[startidx]:
        if nodes[dst][0] > nodes[startidx][0]+cost:
            nodes[dst][0] = nodes[startidx][0]+cost
            nodes[dst][1] = startidx
            heapq.heappush(priority_queue, nodes[dst])
    
    # heapqから一つ取り出し（最小コストの未確定頂点が取り出される）確定させた上で、
    # 新たに確定した点から行ける頂点をキューに入れる
    # これをすべての点が確定するまで繰り返す
    n_done = 1
    while priority_queue:
        if n_done == n_nodes:
            break

        node = heapq.heappop(priority_queue)
        if node[2]: # 確定済みであれば次の頂点を取り出す
            continue
        
        node[2] = True
        n_done += 1

        for dst, cost in graph[node[3]]:
            if nodes[dst][0] > nodes[node[3]][0]+cost:
                nodes[dst][0] = nodes[node[3]][0]+cost
                nodes[dst][1] = node[3]
                heapq.heappush(priority_queue, nodes[dst])

    costs = [node[0] for node in nodes]
    froms = [node[1] for node in nodes]
    return  costs, froms

def resolve():
    N = int(input())
    adjs = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b, c = list(map(int, input().split()))
        adjs[a-1].append([b-1, c])
        adjs[b-1].append([a-1, c])
    Q, K = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    costs, _ = dijkstra_list(adjs, K-1)
    for q in queries:
        print(costs[q[0]-1]+costs[q[1]-1])


if '__main__' == __name__:
    resolve()