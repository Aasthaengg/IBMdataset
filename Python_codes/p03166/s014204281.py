import sys

# input処理を高速化する
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    # 隣接リストを作成
    adjacencyList = [[] for _ in range(N)]

    # 距離の情報
    dp = [0] * N

    # 入次数　（いりじすう）
    deg = [0] * N

    for _ in range(M):
        v, nv = map(int, input().split())
        adjacencyList[v-1].append(nv-1)
        #　入次数に1を足す
        deg[nv-1] += 1

    queue = []

    # BFS探索
    # 入次数がゼロの頂点から探索を始める
    for v in range(N):
        if deg[v] == 0:
            queue.append(v)

    while queue:
        # 現在の頂点をqueueからpop
        v = queue.pop(0)
        for nv in adjacencyList[v]:
            # 探索済みの頂点の入次数を減らす
            deg[nv] -= 1

            # 完全に探索済みの頂点の入次数がゼロの時、経路の距離を出発点から計算
            if deg[nv] == 0:
                # 頂点をqueueに追加する
                queue.append(nv)
                dp[nv] = max(dp[v] + 1, dp[nv])

    print(max(dp))
    
main()