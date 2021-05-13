from collections import deque
N = int(input())

G = {k: [] for k in range(N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    # 無向グラフ
    G[a].append(b)
    G[b].append(a)

c = sorted([int(i) for i in input().split()], reverse=True)

visited = [-1] * N
cnt = 0
que = deque([1])

while que:
    i = que.popleft()
    visited[i-1] = c[cnt]
    cnt += 1

    for j in G[i]:
        if visited[j-1] == -1:
            que.append(j)

# print(visited)
print(sum(c[1:]))
print(*visited)
