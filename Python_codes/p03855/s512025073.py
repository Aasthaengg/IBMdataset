import collections

NO_OF_DIMENSIONS = 2
no_of_edges_by_dim = [None] * NO_OF_DIMENSIONS
n, no_of_edges_by_dim[0], no_of_edges_by_dim[1] = (int(x) for x in input().split())

graph_by_dimension = [[[] for _ in range(n + 1)] for _ in range(NO_OF_DIMENSIONS)]

for dimension, no_of_edges in enumerate(no_of_edges_by_dim):
    graph = graph_by_dimension[dimension]
    for _ in range(no_of_edges):
        p, q = (int(x) for x in input().split())
        graph[p].append(q)
        graph[q].append(p)

components_ids_by_vertex = [[None] * NO_OF_DIMENSIONS for _ in range(n + 1)]

def dfs(dimension_id, vertex_id, colour):
    stack = [vertex_id]
    while len(stack):
        vertex_id = stack.pop()
        components_ids_by_vertex[vertex_id][dimension_id] = colour
        for s in graph_by_dimension[dimension_id][vertex_id]:
            if not components_ids_by_vertex[s][dimension_id]:
                stack.append(s)

for i in range(NO_OF_DIMENSIONS):
    for j in range(1, n + 1):
        if not components_ids_by_vertex[j][i]:
            dfs(i, j, j)

components_ids_by_vertex = [tuple(x) for x in components_ids_by_vertex]

results = collections.Counter(components_ids_by_vertex)

for i in range(1, n + 1):
    print(results[components_ids_by_vertex[i]], end=' ')
print()
