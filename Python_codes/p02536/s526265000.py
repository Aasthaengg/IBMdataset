
N, M = map(int, input().split())

# cities = [[0] * N for i in range(N)]
# print(cities)
cities = {}
 
for a in range(N):
    cities[a+1] = []
# print(cities)
 
for i in range(M):
    i1, i2 = map(int, input().split())
    cities[i1].append(i2)
    cities[i2].append(i1)
# print(cities)
def connected_components(graph):
    seen = set()
    def component(n):
        nodes = set([n])
        while nodes:
            n = nodes.pop()
            seen.add(n)
            nodes |= set(graph[n]) - seen
            yield n
    for n in graph:
        if n not in seen:
            yield component(n)
print(len([list(x) for x in connected_components(cities)])-1)