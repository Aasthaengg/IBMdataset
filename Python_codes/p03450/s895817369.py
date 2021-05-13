from collections import deque

n, m = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(m):
    L, R, D = map(int, input().split())
    tree[L - 1].append((R - 1, D))
    tree[R - 1].append((L - 1, -D))
visited = [None for _ in range(n)]


def bfs(u):
    q = deque([[u, 0]])
    visited[u] = 0
    while q:
        u, dist = q.popleft()
        for next_u, d in tree[u]:
            next_x = dist + d
            if visited[next_u] is None:
                visited[next_u] = next_x
                q.append([next_u, next_x])
            elif visited[next_u] == next_x:
                continue
            else:
                print("No")
                exit()


for i in range(n):
    if visited[i] is None:
        bfs(i)
else:
    print('Yes')
