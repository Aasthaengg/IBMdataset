mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    # return: articulation points, bridges
    # The graph must be connected.
    def lowlink(adj, root=1):
        N = len(adj) - 1
        order = [N + 1] * (N + 1)
        low = [N + 1] * (N + 1)
        AP = []
        bridge = []

        st = [root]
        cnt = 1
        par = [0] * (N + 1)
        seq = []
        while st:
            v = st.pop()
            if order[v] != N+1:
                continue
            order[v] = cnt
            seq.append(v)
            low[v] = cnt
            cnt += 1
            for u in adj[v]:
                if order[u] < cnt:
                    if par[v] != u:
                        low[v] = min(low[v], order[u])
                        continue
                else:
                    par[u] = v
                    st.append(u)

        child = [[] for _ in range(N + 1)]
        for v in range(1, N + 1):
            child[par[v]].append(v)

        seq.reverse()
        for v in seq:
            for u in child[v]:
                low[v] = min(low[v], low[u])

        # bridge
        for p in range(1, N+1):
            for c in child[p]:
                if order[p] < low[c]:
                    bridge.append((p, c))

        # articulation point
        for v in range(1, N + 1):
            if v == root:
                if len(child[v]) > 1:
                    AP.append(v)
            else:
                for c in child[v]:
                    if order[v] <= low[c]:
                        AP.append(v)
                        break

        return AP, bridge

    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    AP, bridge = lowlink(adj)
    print(len(bridge))


if __name__ == '__main__':
    main()
