from collections import deque
n = int(input())
edges = [[]*n for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    edges[a-1].append([b-1, c])
    edges[b-1].append([a-1, c])

q, k = map(int, input().split())
k -= 1
d = deque([k])
visited = [False]*n
visited[k] = True
distance_from_k = [0]*n
while d:
    p = d.popleft()
    for child, c in edges[p]:
        if visited[child]:
            continue
        visited[child] = True
        d.append(child)
        distance_from_k[child] += distance_from_k[p] + c
#print(distance_from_k)

for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(distance_from_k[x] + distance_from_k[y])


