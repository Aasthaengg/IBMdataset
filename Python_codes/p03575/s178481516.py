import networkx as nx

n, m = map(int, input().split())
g = nx.Graph()
g.add_nodes_from(range(1, n + 1))
g.add_edges_from([tuple(map(int, input().split())) for i in range(m)])

print(len(tuple(nx.bridges(g))))