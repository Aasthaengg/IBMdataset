import networkx as nx
import sys

G = nx.Graph()

n, m = map(int, input().split())
if m == 0:
    print(1)
    sys.exit()
for i in range(m):
    a, b = map(int, input().split())
    G.add_edge(a, b)

largest_cc = max(nx.connected_components(G), key=len)
print(len(largest_cc))
