from collections import deque

N, M = list(map(int, input().split()))
graph = [deque() for i in range(N*3)]
visited = [False] * (N*3)

for i in range(M):
    u, v = list(map(int, input().split()))
    u, v = (u-1)*3, (v-1)*3

    graph[u].append(v+1)
    graph[u+1].append(v+2)
    graph[u+2].append(v)

S, T = list(map(int, input().split()))
S, T = (S-1)*3, (T-1)*3

q = deque([(S, 0)])
visited[S] = True
ans = -1

while q:
    u, cost = q.popleft()
    if u == T:
        ans = cost//3
        break
    else:
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append((v, cost+1))
print(ans)