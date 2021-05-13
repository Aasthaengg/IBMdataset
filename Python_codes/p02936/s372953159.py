def resolve():
    N, Q = list(map(int, input().split()))
    adjs = [set() for _ in range(N)]
    for _ in range(N-1):
        src, dst = list(map(int, input().split()))
        adjs[src-1].add(dst-1)
        adjs[dst-1].add(src-1)
    costs = [0 for _ in range(N)]
    for i in range(Q):
        idx, cost = list(map(int, input().split()))
        idx = idx - 1
        costs[idx] += cost
    
    q = [0]
    visited = set()
    while q:
        node = q.pop()
        for nxt in adjs[node]:
            if nxt in visited:
                continue
            costs[nxt] += costs[node]
            q.append(nxt)
        visited.add(node)
    print(*costs)


if '__main__' == __name__:
    resolve()
