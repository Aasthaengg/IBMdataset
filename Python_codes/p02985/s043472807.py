# 解説AC
MOD = 10**9 + 7
m = 10**5 + 5
fac = [0] * m
finv = [0] * m
inv = [0] * m


def COMBinitialize(m):
    fac[0] = 1
    finv[0] = 1
    if m > 1:
        fac[1] = 1
        finv[1] = 1
        inv[1] = 1
        for i in range(2, m):
            fac[i] = fac[i-1] * i % MOD
            inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
            finv[i] = finv[i - 1] * inv[i] % MOD


COMBinitialize(m)


def main():
    N, K = (int(i) for i in input().split())
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = (int(i) for i in input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    acc = [1]*N
    from collections import deque

    def bfs(G, s):
        dist = [-1 for _ in range(N)]
        que = deque()
        dist[s] = 0
        c = len(edge[s]) - 1
        d = len(edge[s]) + 1
        if K < d:
            acc[s] = 0
            return
        acc[s] = fac[K] * finv[K - d]
        acc[s] %= MOD
        que.append(s)
        while que:
            u = que.popleft()
            c = len(edge[u]) - 1
            if K-2 < c:
                acc[u] = 0
                return
            if dist[u] >= 1 and c > 0:
                acc[u] = fac[(K-2)] * finv[(K-2) - c]
                acc[u] %= MOD
            for v in G[u]:
                if dist[v] != -1:
                    continue
                dist[v] = dist[u] + 1
                que.append(v)

    bfs(edge, 0)
    ans = 1
    for a in acc:
        ans *= a
        ans %= MOD
    print(ans % MOD)


if __name__ == '__main__':
    main()
