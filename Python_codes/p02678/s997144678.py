import networkx as nx
n, m, *AB = map(int, open(0).read().split())
G = nx.Graph()
G.add_nodes_from(range(1, n+1))
G.add_edges_from(zip(AB[::2], AB[1::2]))
print('Yes')
d = dict(nx.bfs_predecessors(G, 1))
for i in range(2, n+1):
    print(d[i])