from collections import deque

n, m = map(int, input().split())
e = [list(map(int, input().split())) for _ in range(m)]

res = 0
for i in range(m):
    edge = [[] for _ in range(n)]
    for j in range(m):
        if i == j:
            continue
        a, b = e[j]
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    
    flag = False
    for j in range(n):
        d = deque([j])
        visited = [False] * n
        visit_cnt = 0
        while d:
            node = d.popleft()
            visited[node] = True
            visit_cnt += 1
            for next_node in edge[node]:
                if not visited[next_node]:
                    d.append(next_node)
        if visit_cnt < n:
            flag = True
            break
    
    if flag:
        res += 1

print(res)