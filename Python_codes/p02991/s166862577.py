def main():
    N, M = map(int, input().split())
    d = {}
    for _ in range(M):
        u, v = map(int, input().split())
        if u in d:
            d[u].append(v)
        else:
            d[u] = [v]
    s, t = map(int, input().split())
    cur = set([s])
    ne1 = set()
    ne2 = set()
    ne3 = set()
    c = 0
    v3 = set()
    v1 = set()
    v2 = set()
    while len(v3) < N:
        for i in cur:
            if i not in d:
                continue
            for j in d[i]:
                if j not in v1:
                    ne1.add(j)
                    v1.add(j)
        if len(ne1) == 0:
            return -1
        for i in ne1:
            if i not in d:
                continue
            for j in d[i]:
                if j not in v2:
                    ne2.add(j)
                    v2.add(j)
        if len(ne2) == 0:
            return -1
        for i in ne2:
            if i not in d:
                continue
            for j in d[i]:
                if j not in v3:
                    ne3.add(j)
                    v3.add(j)
        if len(ne3) == 0:
            return -1
        c += 1
        if t in ne3:
            return c
        cur = ne3
        ne1 = set()
        ne2 = set()
        ne3 = set()
    return -1
print(main())
