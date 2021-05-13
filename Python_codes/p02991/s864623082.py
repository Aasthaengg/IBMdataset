def dist(s, t, g):
    q = [s]
    dists = [-1]*len(g)
    dists[s] = 0
    while len(q) != 0:
        p = []
        for u in q:
            for v in g[u]:
                if dists[v] != -1:
                    continue
                p.append(v)
                dists[v] = dists[u] + 1
        q = p
    return dists[t]

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n*3)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v+n)
        g[u+n].append(v+2*n)
        g[u+2*n].append(v)
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    print(dist(s, t, g)//3)

if __name__ == "__main__":
    main()
