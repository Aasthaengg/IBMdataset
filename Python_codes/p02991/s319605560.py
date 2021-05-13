def main():
    N, M = map(int, input().split())
    U = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        U[u - 1].add(v - 1)
    S, T = map(int, input().split())
    S, T = S - 1, T - 1
    V = [False] * N
    V[S] = True
    cur = set([S])
    r = 0
    while cur and T not in cur:
        r += 1
        for _ in range(3):
            nxt = set()
            for c in cur:
                nxt |= U[c]
            cur = nxt
        nxt = set()
        for c in cur:
            if not V[c]:
                V[c] = True
                nxt.add(c)
        cur = nxt
    return r if T in cur else -1

print(main())
