def shortest_path(s,n,w,es):
    #s→iの最短距離
    # s:始点, n:頂点数, w:辺の数, es[i]: [辺の始点,辺の終点,辺のコスト]
    d = [float("inf")] * n
    #d[i] : s→iの最短距離
    d[s] = 0
    for _ in [0]*n:
        update = False
        for p,q,r in es:
            # e: 辺iについて [from,to,cost]
            if d[p] != float("inf") and d[q] > d[p] + r:
                d[q] = d[p] + r
                update = True
        if not update:
            break
    return d

def main():
    import sys
    input = sys.stdin.readline
    n,m,p = map(int,input().split())
    es = []
    edge = [[] for _ in range(n)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        es.append([a-1,b-1,p-c])
        edge[b-1].append(a-1)
    
    ren = [False]*n
    tank = [n-1]
    while len(tank) != 0:
        new = []
        for elt in tank:
            for go in edge[elt]:
                if ren[go]:
                    continue
                ren[go] = True
                new.append(go)
        tank = new

    d = shortest_path(0,n,m,es)

    for p,q,r in es:
        # e: 辺iについて [from,to,cost]
        if d[p] != float("inf") and d[q] > d[p] + r:
            d[q] = d[p] + r
            if ren[q]:
                print(-1)
                exit()

    print(max(-d[-1],0))

if __name__ == '__main__':
    main()