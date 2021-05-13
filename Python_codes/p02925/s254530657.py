from collections import deque
n = int(input())
graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
indeg = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    a = tuple(map(int, input().split()))
    for j, v in enumerate(a):
        if j == n-2:
            continue
        tmp = (min(i, a[j+1]), max(i, a[j+1]))
        indeg[tmp[0]][tmp[1]] += 1
        if i < v:
            graph[i][v].append(tmp)
        else:
            graph[v][i].append(tmp)

cnt = n * (n-1)//2
q = deque([])
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if indeg[i][j] == 0:
            q.append((i, j, 1))
            cnt -= 1

ans = -1
while q:
    x, y, day = q.popleft()
    # print(x, y, day)
    ans = max(ans, day)
    for p, r in graph[x][y]:
        if indeg[p][r] == 0:
            continue
        indeg[p][r] -= 1
        if indeg[p][r] == 0:
            q.append((p, r, day+1))
            cnt -= 1

if cnt == 0:
    print(ans)
else:
    print(-1)