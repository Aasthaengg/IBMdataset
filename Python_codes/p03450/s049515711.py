import sys
n, m = map(int, input().split())
if m==0:
    print("Yes")
    sys.exit()

tree = [[] for _i in range(n+1)]
for _i in range(m):
    l, r, d = map(int, input().split())
    tree[l].append([r, d])
    tree[r].append([l, -d])

from collections import deque
INF = "INF"
visit = [INF for _i in range(n+1)]
for i in range(1, n+1):
    if visit[i]==INF:
        visit[i] = 0
    else:
        continue
    q = deque([i])
    while q:
        p = q.popleft()
        if visit[p]==INF:
            visit[p] = 0
        for i, j in tree[p]:
            if i==p:
                continue
            elif visit[i] == INF:
                visit[i] = visit[p]+j
                q.append(i)
            elif visit[i] == visit[p]+j:
                continue
            else:
                print("No")
                sys.exit()

print("Yes")