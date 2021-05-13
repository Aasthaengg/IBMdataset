import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines



def main():
    #距離が3の倍数である経路のうち最短である経路が存在するかどうかを調べる
    #存在するときその経路の距離を3で割った商が答え
    #存在しないとき-1を出力する

    #経路の距離を3で割った余りで頂点の状態を分類する

    #与えられたグラグをGとする
    #Gの辺の張っている隣接頂点u,vを考える
    #Gは有効グラフであるからu->vの様に辺が張っているとする
    #次のようにグラフGの頂点拡張する
    #(u, r) := uへたどり着く最短経路を3で割ったときr余る状態（状態を頂点とした新たなグラフG'を考えることになる）
    #辺の重みは1であるので(u, 0)->(v, 1), (u, 1)->(v, 2), (u, 2) -> (v, 0)の状態遷移が考えられる
    #（例：余り0から1移動すれば経路は1伸びるから全経路を3で割った余りは1となる）

    #(S, 0) -> ... ->(T, 0)となる最短経路が「距離が3の倍数である経路のうち最短である経路」である

    N, M = map(int, readline().split())
    to = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, readline().split())
        u-=1
        v-=1
        to[u].append(v)
    S, T = map(int, readline().split())
    S-=1
    T-=1

    INF = int(1e9)
    #距離を3で割った余りで分類して状態の遷移を考える
    dist = [[INF for _ in range(3)] for _ in range(N)]     

    #BFS
    from collections import deque
    dq = deque()
    dq.append((S, 0))
    dist[S][0] = 0
    while len(dq)>0:
        v, r = dq.popleft() 
        for nxv in to[v]:
            nxr = (r+1)%3
            if dist[nxv][nxr] != INF:
                continue
            dist[nxv][nxr] = dist[v][r] + 1
            dq.append((nxv, nxr))

    if dist[T][0] == INF:
        print(-1)
    else:
        print(dist[T][0]//3)
if __name__ == '__main__':
    main()
