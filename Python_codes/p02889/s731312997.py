INF = float('inf')

def warshall_floyd(G):
    # ワーシャルフロイド法で移動距離を求める
    # G[x][y]: xからyへ直接移動するときの距離。直接移動できない場合はINF
    # 
    cost = [g[:] for g in G]
    N = len(G)
    # cost[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][k] != INF and cost[k][j] != INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost

def main():
    N, M, L = map(int, input().split())

    # G[x][y]: xからyへ直接移動するときのコスト。移動できない場合はINF
    G = [[INF] * (N+1) for n in range(N+1)]

    for i in range(M):
        a, b, c = map(int, input().split())
        G[a][b] = c
        G[b][a] = c

    Q = int(input())
    Queries = []
    for i in range(Q):
        s, t = map(int, input().split())
        Queries.append((s, t))

    # ワーシャルフロイド法で、全点間の距離を求める
    cost = warshall_floyd(G)

    # 全点間の距離のうち、移動距離がL以内でおさまる頂点同士は、給油せずにすむ
    # そこで、全点間の距離のうち、移動距離がL以内でおさまる頂点同士を距離1で結んだグラフを作成し、
    # そのグラフに対してワーシャルフロイド法で最短距離を計算することで、
    # refuel[x][y] =「xからyへ移動するときの給油回数+1」というグラフを作成できる
    no_refuel = [[1 if x <= L else INF for x in c] for c in cost]

    refuel_count = warshall_floyd(no_refuel)

    ans = []
    for s, t in Queries:
        d = refuel_count[s][t]
        ans.append(d-1 if d != INF else -1)
    
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()