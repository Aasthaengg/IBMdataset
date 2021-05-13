from collections import defaultdict, deque
N,M=map(int, input().split())
G = {i: [] for i in range(1, N+1)}
deg = [0]*(N+1)
for _ in range(M):
    x,y=map(int,input().split())
    G[x].append(y)
    deg[y] += 1

from collections import deque, defaultdict
S = [i for i in range(1, N+1) if deg[i]==0]
dp = [0]*(N+1)

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
    def bfs():
        """
        sからBFSする
        """
        queue = deque(S)
        while queue:
            u = queue.popleft()
            # queueには入次数0のノードが入っているのでretに追加
            # ret.append(u)

            for v in adj[u]: # uの子ノードを探索
                indeg[v] -= 1 #探索したら子の次数を減らす
                if (indeg[v] == 0):
                    # 入次数0かつ未訪問なら
                    queue.append(v)
                    dp[v] = max(dp[v], dp[u]+1)
                    is_visited[v] = 1
    
    bfs()
    
    # return ret

topological_sort(G, deg)
print(max(dp))