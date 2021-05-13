edges = list(map(int, input().split(' ')))

longest = max(edges)
edges.remove(longest)

print(edges[0] * edges[1] // 2)
