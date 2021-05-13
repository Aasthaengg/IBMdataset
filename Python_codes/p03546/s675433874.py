def warshall_floyd(graph):
    # 頂点数
    n_nodes = len(graph)

    froms = []
    # fromsの初期化
    for i in range(len(graph)):
        froms.append([])
        for j in range(len(graph[i])):
            if i == j:                          # 同じ点にかえって来る場合  
                froms[i].append(0)
            elif graph[i][j] < float("inf"):    # i -> j間に辺がある場合、ひとまずiをdestに行く直前のnodeとしておく
                froms[i].append(i)
            else:
                froms[i].append(None)

    # 更新
    for k in range(n_nodes):
        for i in range(n_nodes):
            for j in range(n_nodes):
                adj_cost = graph[i][k] + graph[k][j]
                if adj_cost < graph[i][j]:
                    # i -> jの最短経路は i -> k -> jであることを意味する
                    # よってjの直前に立ち寄る頂点は k -> j の最短経路においてjの直前に寄る点である
                    graph[i][j] = adj_cost
                    froms[i][j] = froms[k][j]
    
    has_negative_loop = False
    for i in range(n_nodes):
        if graph[i][i] < 0:
            has_negative_loop = True
            break

    return graph, froms, has_negative_loop


def resolve():
    H, W = list(map(int, input().split()))
    C = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]
    C, _, __ = warshall_floyd(C)
    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] == -1:
                continue
            ans += C[A[i][j]][1]
    print(ans)

        

if '__main__' == __name__:
    resolve()