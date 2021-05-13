def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M, P = (int(i) for i in input().split())
    adj_list = [[] for _ in range(N)]
    radj_list = [[] for _ in range(N)]
    ok = [False]*N
    edge = []
    for i in range(M):
        a, b, c = (int(i) for i in input().split())
        c -= P
        adj_list[a-1].append(b-1)
        radj_list[b-1].append(a-1)
        edge.append((a-1, b-1, -c))

    def dfs(G, v):
        seen = [False]*N
        todo = [v]
        seen[v] = True
        while todo:
            u = todo.pop()
            for next_v in G[u]:
                if seen[next_v]:
                    continue
                seen[next_v] = True
                todo.append(next_v)
        return seen

    i = 0
    for s, rs in zip(dfs(adj_list, 0), dfs(radj_list, N-1)):
        ok[i] = s and rs
        i += 1

    # Bellman_ford
    d = [10**12]*N
    d[0] = 0
    update = True
    step = 0
    while update:
        update = False
        for a, b, c in edge:
            if not(ok[a]) or not(ok[b]):
                continue
            newD = d[a] + c
            if newD < d[b]:
                update = True
                d[b] = newD
        step += 1
        if step > N:
            return print(-1)
    print(max(0, d[N-1]*-1))


if __name__ == '__main__':
    main()
