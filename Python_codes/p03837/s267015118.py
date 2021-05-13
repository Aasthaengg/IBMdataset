import sys
def input(): return sys.stdin.readline().strip()
INF = 10**18

def main():
    N, M = map(int, input().split())
    repn = [[] for _ in range(N)]
    edge = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        repn[a - 1].append((c, b - 1))
        repn[b - 1].append((c, a - 1))
        edge.append((a - 1, b - 1, c))

    # 全点間最短距離をワーシャルフロイドで求める
    dist = [[INF] * N for _ in range(N)]
    for i in range(N): dist[i][i] = 0
    for i in range(N):
        for cost, j in repn[i]: dist[i][j] = cost

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 辺を一つずつ見て余分かどうか判定する
    ans = 0
    for a, b, c in edge:
        no_need = True
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][a] + (c - 1) + dist[b][j]:
                    no_need = False
                    break
        if no_need: ans += 1
    print(ans)



if __name__ == "__main__":
    main()
