import networkx as nx
a=[[int(i) for i in input().split()] for _ in range(3)]
g = nx.Graph()
for x in a:
     g.add_edge(x[0],x[1])
print("YES" if nx.is_semieulerian(g) else "NO")