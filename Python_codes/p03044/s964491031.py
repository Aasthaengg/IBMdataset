n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    tree[u].append([v, w])
    tree[v].append([u, w])

color = [-1] * (n+1)
color[1] = 0
stack = [1]

while stack:
    node = stack.pop()
    for vertex, weight in tree[node]:
        if color[vertex] != -1:
            continue
        color[vertex] = (color[node] + weight) % 2
        stack.append(vertex)

print("\n".join(map(str, color[1:])))



