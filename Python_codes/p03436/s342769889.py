import networkx as nx
import numpy as np

h, w, *X, = open(0).read().split()
h, w = int(h), int(w)

G = nx.grid_2d_graph(h, w)
for i, S in enumerate(X):
    for j, s in enumerate(S):
        if s == '#':
            G.remove_node((i, j))
try:
    path = nx.shortest_path(G, (0, 0), (h-1, w-1))
except nx.NetworkXNoPath:
    print(-1)
else:
    for node in path:
        G.remove_node(node)
    print(len(G.nodes))