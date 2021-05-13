N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    edges.append((a, b))

parent = [i for i in range(N)]
height = [1] * N

def find(i):
    while i != parent[i]:
        i = parent[i]
    return i

def union(i, j):
    i = find(i)
    j = find(j)
    if height[i] >= height[j]:
        parent[j] = i
        height[i] = max(height[i], height[j] + 1)
    else:
        parent[i] = j
        height[j] = max(height[j], height[i] + 1)

bridges = 0
for cand in range(M):
    parent = [i for i in range(N)]
    height = [1] * N
    islands = N
    for i in range(M):
        if i == cand:
            continue
        a, b = edges[i]
        if find(a) == find(b):
            continue
        islands -= 1
        union(a, b)
    if islands > 1:
        bridges += 1
print(bridges)

