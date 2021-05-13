import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def abc079_d():
    inp = iter(map(int, read().split()))
    H, W = next(inp), next(inp)
    adj_mtx = [[next(inp) for _ in range(10)] for _ in range(10)]
    grid = [[next(inp) for _ in range(W)] for _ in range(H)]

    def floyd_warshall(W):
        ''' ワーシャルフロイド法、全頂点間の最短距離 '''
        n = len(W)  # 頂点の数
        # DPで全頂点間の最短距離を求める
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    W[u][v] = min(W[u][v], W[u][k] + W[k][v])
        return W

    min_dist = floyd_warshall(adj_mtx)

    # グリッドの数字が-1と1以外はコスト発生するため足していく
    ans = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == -1 or grid[i][j] == 1:
                continue
            ans += min_dist[grid[i][j]][1]
    print(ans)

abc079_d()