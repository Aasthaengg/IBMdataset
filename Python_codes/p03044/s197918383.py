from collections import deque
N = int(input())
UVW = [list(map(int, input().split())) for _ in range(N-1)]
G = [{} for _ in range(N+1)]
for u, v, w in UVW:
    G[u-1][v-1] = w
    G[v-1][u-1] = w
# print(G)


distance = [-1] * N

que = deque([(0, 0)])
while que:
    c, d = que.popleft()
    distance[c] = d

    for n, w in G[c].items():
        if distance[n] == -1:
            que.append((n, d+w))

# print(distance)
print(*[d % 2 for d in distance], sep='\n')
