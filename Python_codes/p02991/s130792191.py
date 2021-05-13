from collections import deque

#create digraph
#nodes will be (steps % 3) * N + node
N, M = map(int, input().split())
adj = [[] for _ in range(3*N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    adj[      u].append(  N + v)
    adj[  N + u].append(2*N + v)
    adj[2*N + u].append(      v)

S, T = map(int, input().split())
S -= 1
T -= 1

#bfs
q = deque([S])
depth = [10 ** 9] * (3*N)
depth[S] = 0
while q:
    node = q.popleft()
    if node == T:
        break
    for next_node in adj[node]:
        if depth[next_node] > depth[node] + 1:
            depth[next_node] = depth[node] + 1
            q.append(next_node)

if depth[T] == 10 ** 9:
    print(-1)
else:
    print(depth[T] // 3)