def c_bridge_networkx():
    import networkx as nx
    N, M = [int(i) for i in input().split()]
    Edges = [tuple([int(i) for i in input().split()]) for j in range(M)]

    graph = nx.Graph()
    graph.add_nodes_from(range(1, N + 1))
    graph.add_edges_from(Edges)
    # bridges(graph): graph の橋になる辺を結ぶ頂点の組を返す
    return len(tuple(nx.bridges(graph)))

print(c_bridge_networkx())