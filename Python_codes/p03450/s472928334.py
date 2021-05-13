def resolve():
    N, M = list(map(int, input().split()))
    LRD = [list(map(int, input().split())) for _ in range(M)]
    adj_list = [[] for _ in range(N)]
    for lrd in LRD:
        l, r, d = lrd
        adj_list[l-1].append((l-1, r-1, d))
        adj_list[r-1].append((r-1, l-1, -d))
    
    X = [None]*N
    import collections

    for i in range(N):
        if X[i] is not None:
            continue
        q = collections.deque(adj_list[i])
        X[i] = 0
        while q:
            src, nxt, d = q.pop()
            if X[nxt] is not None:
                if X[nxt] != X[src] + d:
                    print("No")
                    return
            else:
                X[nxt] = X[src] + d
                q.extend(adj_list[nxt])
    print("Yes")

    


if '__main__' == __name__:
    resolve()
