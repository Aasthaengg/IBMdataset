from collections import deque

n, m = map(int, input().split())
People = {x+1:[] for x in range(10**6+1)}

for _ in range(m):
    l, r, d = map(int, input().split())
    People[l].append([r, d])
    People[r].append([l, -d])

INF = 10**10
Visited = [INF for i in range(10**6+1)]

def bfs(v):
    dq = deque()
    dq.append(v)
    Visited[v] = 0
    check = True
    while dq:
        now = dq.popleft()
        Related = People[now]
        for related in Related:
            if Visited[related[0]] == INF:
                dq.append(related[0])
                Visited[related[0]] = Visited[now] + related[1]
            elif Visited[related[0]] != Visited[now] + related[1]:
                check = False
    return check

ans = 'Yes'
for i in range(1,10**6+1):
    if Visited[i] == INF:
        if bfs(i) == False:
            ans = 'No'

print(ans)

