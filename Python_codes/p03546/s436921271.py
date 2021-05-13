import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def abc079_d():
    inp = iter(map(int, read().split()))
    H, W = next(inp), next(inp)
    adj_mtx = [[next(inp) for _ in range(10)] for _ in range(10)]
    grid = [[next(inp) for _ in range(W)] for _ in range(H)]

    import heapq
    def dijkstra(start, W):
        ''' スタート地点から到達可能なすべての頂点への最短距離を返す
            Pythonで学ぶアルゴリズムとデータ構造 P.111 一部変更
        '''
        # 仮の最短距離をinfに設定
        inf = 10**9
        distance_list = [inf] * len(W)
        # スタートの頂点だけ距離を0にする
        distance_list[start] = 0
        # 最短距離が確定した点
        done_list = []
        # 次に処理する頂点を決めるためのヒープ
        wait_heap = []
        for i, d in enumerate(distance_list):
            # (スタートからの距離, 頂点) のタプル
            heapq.heappush(wait_heap, (d, i))
        # ヒープが空になるまで処理を続ける
        while wait_heap:
            p = heapq.heappop(wait_heap)
            i = p[1]
            if i in done_list:
                continue
            # この時点でスタートからiへの距離が確定する
            done_list.append(i)
            # iに隣接するすべての頂点に対する処理
            for j, x in enumerate(W[i]):
                if x > -1 and j not in done_list:
                    # 緩和
                    d = min(distance_list[j], distance_list[i] + x)
                    distance_list[j] = d
                    # jへの仮の最短距離をdとしてヒープに追加
                    heapq.heappush(wait_heap, (d, j))
        return distance_list

    # 各点から1への距離(コスト)
    dist_to_1 = [None] * 10
    for i in range(10):
        dist_to_1[i] = dijkstra(i, adj_mtx)[1]

    # グリッドの数字が-1と1以外はコスト発生するため足していく
    ans = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == -1 or grid[i][j] == 1:
                continue
            ans += dist_to_1[grid[i][j]]
    print(ans)

abc079_d()