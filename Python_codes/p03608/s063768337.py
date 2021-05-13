def warshall_floyd(graph):
    n_nodes = len(graph)

    froms = []
    for i in range(len(graph)):
        froms.append([])
        for j in range(len(graph[i])):
            if i == j:                          # 同じ点にかえって来る場合  
                froms[i].append(0)
            elif graph[i][j] < float("inf"):    # i -> j間に辺がある場合、ひとまずiをdestに行く直前のnodeとしておく
                froms[i].append(i)
            else:
                froms[i].append(None)

    for k in range(n_nodes):
        for i in range(n_nodes):
            for j in range(n_nodes):
                adj_cost = graph[i][k] + graph[k][j]
                if adj_cost < graph[i][j]:
                    graph[i][j] = adj_cost
                    froms[i][j] = froms[k][j]
    
    has_negative_loop = False
    for i in range(n_nodes):
        if graph[i][i] < 0:
            has_negative_loop = True
            break

    return graph, froms, has_negative_loop

def resolve():
    N, M, R = list(map(int, input().split()))
    R = list(map(int, input().split()))
    adjs = [[float("inf") for _ in range(N)] for __ in range(N)]
    for i in range(M):
        a, b, c = list(map(int, input().split()))
        adjs[a-1][b-1] = c
        adjs[b-1][a-1] = c
    costs, _, __ = warshall_floyd(adjs)
    
    import itertools
    mincost = float("inf")
    for route in itertools.permutations(R):
        src = route[0] - 1
        cost = 0
        for didx in range(1, len(route)):
            dst = route[didx] - 1
            cost += costs[src][dst]
            src = dst
        mincost = min(mincost, cost)
    print(mincost)
    
        

if '__main__' == __name__:
    resolve()