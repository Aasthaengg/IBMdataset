(N, _), *edges = [map(int, s.split()) for s in open(0)]
graph = {i: [] for i in range(N)}
for a, b in edges:
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
print("\n".join(str(len(graph[i])) for i in range(N)))
