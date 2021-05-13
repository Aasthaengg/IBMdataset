from collections import deque
N = int(input())

G = {k: [] for k in range(N)}
for _ in range(N-1):
    a, b = map(int, input().split())
    # 無向グラフ
    G[a-1].append(b-1)
    G[b-1].append(a-1)


def bfs(i):
    visited = [-1 for _ in range(N)]
    visited[i] = 0
    que = deque([(i, 0)])

    while que:
        ci, d = que.popleft()

        for ni in G[ci]:
            if visited[ni] == -1:
                visited[ni] = d+1
                que.append((ni, d+1))

    return visited


F = bfs(0)
S = bfs(N-1)


ans = 0
for i in range(N):
    if F[i] <= S[i]:
        ans += 1
    else:
        ans -= 1
if ans > 0:
    print('Fennec')
else:
    print('Snuke')
