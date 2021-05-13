N, M = map(int, input().split())

con = [[0]*(N+1) for _ in range(N+1)]
edge = []
for i in range(M):
    a, b = map(int, input().split())
    con[a][b] = con[b][a] = 1
    edge.append((a, b))

def floodfill(listz, comp):
    cnt = 0
    #print('comp = {}'.format(comp))
    while len(listz):
        newlistz = []
        for node in listz:
            compo[node] = comp
            cnt += 1
            #print(node)
            for i in range(1, N+1):
                if visited[i] == 0 and con[node][i] > 0:
                    visited[i] = 1
                    newlistz.append(i)
        listz = newlistz

    return cnt

ans = 0

for kk in range(M):
    a, b = edge[kk]
    con[a][b] = con[b][a] = 0
    #print('cut edge{} {}'.format(a, b))
    visited = [0] * (N + 1)
    compo = [0] * (N + 1)
    compID = 0
    total = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            count = floodfill([i], compID)
            if count > 0:
                compID += 1
                total += count
                if total >= N:
                    break

    if compID > 1:
        ans += 1
    #return
    con[a][b] = con[b][a] = 1


print(ans)
