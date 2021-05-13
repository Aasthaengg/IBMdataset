N, M = list(map(int,input().split()))
graph = [[-1 for i in range(N)] for i in range(N)]
in_list = []
for i in range(M):
    a, b = list(map(int,input().split()))
    in_list.append([a, b])
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
    
# 頂点 node を含む連結成分が木なら 1 を返す
def dfs(node, parent):
    ret = 1
    global seen
    if seen[node]:  return 0
    seen[node] = True
    for i in range(N):
        if graph[node][i] == 1 and i != parent:
            ret = min(dfs(i, node), ret)
    return ret

ans = 0

for i in range(M):
    
    graph[in_list[i][0] - 1][in_list[i][1] - 1] = -1
    graph[in_list[i][1] - 1][in_list[i][0] - 1] = -1
    
    seen = [False for _ in range(N)]
    link = 0 # 連結成分
    wood = 0 # 木の個数
    
    for j in range(N):
        if seen[j] == False:
            link += 1
            wood += dfs(j, 0)
            seen[j] = True
            
    ans += (link != 1)
    
    graph[in_list[i][0] - 1][in_list[i][1] - 1] = 1
    graph[in_list[i][1] - 1][in_list[i][0] - 1] = 1
    
print(ans)