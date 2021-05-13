N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    edges.append((a, b))

parent = [i for i in range(N)]
height = [1] * N
size = [1] * N

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
        size[i] += size[j]
    else:
        parent[i] = j
        height[j] = max(height[j], height[i] + 1)
        size[j] += size[i]


score = N*(N-1)//2
ans = [score]
for a, b in edges[::-1]:
    a = find(a)
    b = find(b)
    if a != b:
        score -= size[a] * size[b]
        union(a, b)
    ans.append(score)

for i in ans[len(ans)-2::-1]:
    print(i)