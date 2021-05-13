N,M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    L,R,D = map(int, input().split())
    G[L-1].append((R-1, D))
    G[R-1].append((L-1, -D))

dist = [0] * N
visited = [False] * N

def dfs(v:int):
    """ 矛盾がある -> True """
    stack = [v]
    dist[v] = 0
    visited[v] = True

    while stack:
        v = stack.pop()
        d = dist[v]
        for to, cost in G[v]:
            if visited[to]:
                if dist[to] != d + cost:
                    return True
            else:
                visited[to] = True
                dist[to] = d + cost
                stack.append(to)
    
    return False

flag = True
for v in range(N):
    if not visited[v]:
        if dfs(v):
            flag = False
            break

if flag:
    print('Yes')
else:
    print('No')