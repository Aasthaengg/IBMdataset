N,M = map(int,input().split())
path = [[] for _ in range(N)]
save = []
for _ in range(M):
    a,b = map(int,input().split())
    save.append([a-1,b-1])
    path[b-1].append(a-1)
    path[a-1].append(b-1)


def dfs(now):
    global cnt
    if not 0 in vis: 
        cnt += 1
        return None
    for new in path[now]:
        if vis[new] == 0:
            vis[new] = 1
            dfs(new)
cnt = 0
for i in range(M):
    vis  = [0 for _ in range(N)]
    a = save[i][0]
    b = save[i][1]
    path[a].remove(b)
    path[b].remove(a)
    vis[0] = 1
    dfs(0)
    path[a].append(b)
    path[b].append(a)
print(M-cnt)

