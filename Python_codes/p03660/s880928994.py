def main():
    from heapq import heappush, heappop
    N = int(input())
    ans = ["Fennec", "Snuke"]
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = (int(i)-1 for i in input().split())
        edge[a].append((1, b))
        edge[b].append((1, a))

    def dijkstra(s):
        """ 始点sから各頂点への最短距離 O((|E|+|V|)log|V|) """
        d = [10**8]*N
        used = [True] * N  # True:未確定
        d[s] = 0
        used[s] = False
        edges = []
        for e in edge[s]:
            heappush(edges, e)
        while len(edges):
            c, v = heappop(edges)
            if not used[v]:
                continue
            d[v] = c
            used[v] = False
            for nexc, nexv in edge[v]:
                if used[nexv]:
                    heappush(edges, (nexc+c, nexv))
        return d

    d_s = dijkstra(0)
    d_g = dijkstra(N-1)
    # print(d_s, d_g, sep="\n")
    get = [0, 0]
    for s, g in zip(d_s, d_g):
        if s <= g:
            get[0] += 1
        else:
            get[1] += 1
    if get[0] > get[1]:
        print(ans[0])
    else:
        # マスの数同じならsnuke win
        print(ans[1])


if __name__ == '__main__':
    main()
