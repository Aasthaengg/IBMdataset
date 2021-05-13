def main():
    from collections import deque
    N, M = (int(i) for i in input().split())
    G = [[] for _ in range(N)]
    deg = [0]*N
    for _ in range(M):
        a, b = (int(i) for i in input().split())
        G[a-1].append(b-1)
        deg[b-1] += 1

    dist = [10**6]*(N)

    def topological_sort():
        """
        deg[i] := 頂点iの入次数
        グラフ入力時に計算
        """
        que = deque()
        for i in range(N):
            if deg[i] == 0:
                que.append(i)
                dist[i] = 0

        while que:
            u = que.popleft()
            for v in G[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    que.append(v)
                    dist[v] = dist[u] + 1

    topological_sort()

    print(max(dist))


if __name__ == '__main__':
    main()
