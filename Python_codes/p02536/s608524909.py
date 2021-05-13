import networkx as nx
N, M = map(int, input().split())

G=nx.Graph()

for _ in range(M):
    a, b = map(int, input().split())
    G.add_edge(a,b)

tmp= list(nx.connected_components(G))

count=0

for i in tmp:
    count+=len(i)


print(N-count+len(tmp)-1)