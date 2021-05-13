from collections import deque, defaultdict

N,M=map(int,input().split())
G=defaultdict(lambda:[])
indeg = [0]*(N+1)
for _ in range(M):
    x,y=map(int,input().split())
    G[x].append(y)
    indeg[y]+=1

def topological_sort(adj, indeg):
    """
    幅優先探索によるトポロジカルソート
    O(|V|+|E|)

    adj: 隣接リスト
    indeg: 各ノード入次数を管理するリスト

    ret: トポロジカルソートされたリスト
    """
    is_visited = [0]*(N+1)
    ret = []

    def bfs(s):
        """
        sからBFSする
        """
        queue = deque([s])
        is_visited[s] = 1
        while queue:
            u = queue.popleft()
            # queueには入次数0のノードが入っているのでretに追加
            ret.append(u)

            for v in adj[u]: # uの子ノードを探索
                indeg[v] -= 1 #探索したら子の次数を減らす
                if (indeg[v] == 0) and (not is_visited[v]):
                    # 入次数0かつ未訪問なら
                    queue.append(v)
                    is_visited[v] = 1
    
    for u in range(1, N+1):
        if (indeg[u]==0) and (not is_visited[u]):
            # 流入0かつ未訪問なら
            bfs(u) # uからBFS
    
    return ret

L = topological_sort(G,indeg.copy())
dp = [0]*(N+1)
for i in range(N):
    node = L[i]
    for nx in G[node]:
        dp[nx] = max(dp[nx], dp[node]+1)
print(max(dp))